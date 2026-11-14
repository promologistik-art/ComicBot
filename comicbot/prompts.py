from __future__ import annotations

from datetime import date


# На старте используем короткие самостоятельные эпизоды одной истории.
# В каждом выпуске меняем позу, одежду, ракурс и окружение, сохраняя лицо.
EPISODES = [
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN. Глава 1: в доме появился загадочный ящик. Никто не помнит, кто его подключил…",
        "prompt": """Create a polished, humorous cinematic comic illustration for a Russian family-tech comedy.
The same woman from the reference image is the main heroine. Preserve her recognizable facial identity and natural facial proportions.
Scene: a cozy modern apartment living room in the evening. The heroine has just discovered a mysterious small elegant black box on a shelf, with a tiny glowing network symbol but absolutely no readable text. She looks at it with curious suspicion, one hand reaching toward it. Show a clear dynamic three-quarter body pose, not a passport portrait.
Outfit: casual stylish home outfit, soft oversized cream cardigan, dark fitted jeans, simple jewelry.
Composition: vertical editorial comic panel, expressive storytelling, warm domestic lighting, detailed but uncluttered background. Keep the heroine's face sharp and recognizable. Add no lettering, captions, logos, watermarks, or speech bubbles.""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN. Глава 2: папа решил, что загадочный ящик — это новый пульт от телевизора.",
        "prompt": """Create a polished, humorous cinematic comic illustration for a Russian family-tech comedy.
Use the woman in the reference image as the same recurring heroine; preserve her recognizable facial identity.
Scene: a modern family living room. The heroine stands beside a television while an older man in the background points a remote control at a small mysterious black network box, clearly confusing the two devices. The heroine reacts with amused disbelief. Dynamic natural pose, heroine shown from knees up, looking toward the man rather than straight into camera.
Outfit: elegant dark green blouse, tailored trousers, delicate silver earrings.
Warm evening interior, expressive visual storytelling, tasteful comic-book rendering with realistic faces and hands. No readable text, no logos, no watermark, no speech bubbles.""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN. Глава 3: мама обнаружила, что интернет теперь работает даже на кухне.",
        "prompt": """Create a polished, humorous cinematic comic illustration for a Russian family-tech comedy.
The recurring heroine is the same woman from the reference image. Preserve her recognizable facial identity.
Scene: bright apartment kitchen in the morning. The heroine is holding a tablet and showing her surprised mother that a video is streaming smoothly; in the background a family member happily uses a laptop. Show the heroine in a lively side-facing pose, gesturing toward the tablet, not standing still for a portrait.
Outfit: light blue shirt with rolled sleeves, dark high-waisted trousers, understated jewelry.
Bright natural daylight, warm family atmosphere, clear visual joke, vertical comic-panel composition, expressive but realistic faces. No readable text, logos, watermark, or speech bubbles.""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN. Глава 4: младший брат подключил к сети всё, что нашёл в квартире.",
        "prompt": """Create a polished, humorous cinematic comic illustration for a Russian family-tech comedy.
Use the exact same recurring heroine from the reference image; preserve her recognizable facial identity.
Scene: a slightly chaotic living room. The heroine stands beside a small network box while a mischievous younger brother proudly presents an absurd collection of connected household gadgets: tablet, laptop, smart speaker, game controller and a desk lamp. The heroine raises one eyebrow and counts the devices on her fingers. Clear dynamic pose, three-quarter view, full upper body visible.
Outfit: burgundy casual jacket over a simple black top, dark trousers.
Playful cinematic lighting, detailed cozy apartment, visual comedy, vertical comic panel. No readable text, no logos, no watermark, no speech bubbles.""",
    },
]


def episode_for_day(day: date) -> dict[str, str]:
    return EPISODES[(day.toordinal() - 1) % len(EPISODES)]
