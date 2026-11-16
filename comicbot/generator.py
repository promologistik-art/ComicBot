from __future__ import annotations

import shutil
import time
from datetime import date
from pathlib import Path

from gradio_client import Client, handle_file

from .config import Settings
from .prompts import episode_for_day


def _result_path(result: object) -> str | None:
    if isinstance(result, str):
        return result
    if isinstance(result, dict):
        return result.get("path") or result.get("name")
    if isinstance(result, (list, tuple)):
        for item in result:
            found = _result_path(item)
            if found:
                return found
    return None


def generate_daily_image(settings: Settings, day: date) -> tuple[Path, str]:
    if not settings.hero_reference.is_file():
        raise FileNotFoundError(
            f"Не найден референс героини: {settings.hero_reference}"
        )

    episode = episode_for_day(day)
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    settings.log_dir.mkdir(parents=True, exist_ok=True)
    output = settings.output_dir / f"comic_{day.isoformat()}.png"

    if output.is_file() and output.stat().st_size > 50_000:
        return output, episode["caption"]

    print("Подключаемся к Qwen-Image-2.1...")
    # gradio_client 1.14.0 uses hf_token; token is the newer constructor name.
    client = Client("Qwen/Qwen-Image-2.1", hf_token=settings.hf_token)

    prepared = client.predict(
        input_images=[{"image": handle_file(str(settings.hero_reference)), "caption": None}],
        original_prompt=episode["prompt"],
        enable_extend=True,
        custom_size=True,
        quality="speed",
        seed=0,
        randomize_seed=True,
        api_name="/prepare_request",
    )
    _, seed, _rewritten_prompt = prepared

    started = time.monotonic()
    result = client.predict(
        original_prompt=episode["prompt"],
        enable_extend=True,
        custom_size=True,
        log_dir=str(settings.log_dir),
        seed=seed,
        height=1280,
        width=960,
        negative_prompt=(
            "different woman, changed identity, changed face, distorted face, "
            "bad anatomy, deformed hands, extra fingers, unreadable text, "
            "letters, watermark, logo, blurry, low quality"
        ),
        api_name="/generate_request",
    )
    print(f"Генерация завершена за {time.monotonic() - started:.1f} сек.")

    source = _result_path(result)
    if not source or not Path(source).is_file():
        raise RuntimeError(f"Qwen не вернул доступный файл изображения: {result!r}")

    temporary = output.with_suffix(".tmp.png")
    shutil.copy2(source, temporary)
    if temporary.stat().st_size < 50_000:
        temporary.unlink(missing_ok=True)
        raise RuntimeError("Полученное изображение подозрительно маленькое.")
    temporary.replace(output)
    return output, episode["caption"]
