from __future__ import annotations

from datetime import date


# Первый сезон: короткие самостоятельные трёхпанельные эпизоды
# одной семейной истории. Постоянная героиня — identity reference.
# Визуальный стиль: оригинальная чёрно-белая ретро-манга,
# ручная тушь, выразительная штриховка, три горизонтальные панели.
EPISODES = [
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 1. В доме появился загадочный ящик. И, кажется, он уже подключён ко всему.",
        "prompt": """Create one complete original black-and-white retro manga comic page with EXACTLY THREE horizontal panels stacked vertically, read from top to bottom. Hand-inked artwork, expressive clean linework, subtle cross-hatching, charming visual comedy, consistent character design across all panels.

The same woman from the reference image is the recurring heroine in every panel. Preserve her recognizable facial identity, facial proportions, hairstyle and chestnut hair, translating her features naturally into manga ink drawing.

STORY — "The mysterious box":
Panel 1: In a cozy modern family apartment at evening, the heroine notices a mysterious small black network box on a shelf. She pauses mid-step and looks at it suspiciously.
Panel 2: Close-up: she leans closer and carefully reaches one finger toward the strange box; a tiny indicator light glows. Her expression changes from curiosity to concern.
Panel 3: Wider view: several household devices around the room suddenly light up at once. The heroine stands in the middle of the room, startled, holding her hands up in disbelief.

Heroine outfit: soft oversized cream cardigan, dark fitted jeans, simple jewelry. Vary her pose naturally between panels; do not make this a fashion portrait.
Make the visual sequence clear and funny. Leave speech balloons empty (no letters or pseudo-text), no captions, no logos, no watermark. Keep the three panel borders clearly separated. Entire comic page must be visible in a vertical composition.""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 2. Папа решил, что загадочный ящик — это новый пульт от телевизора.",
        "prompt": """Create one complete original black-and-white retro manga comic page with EXACTLY THREE horizontal panels stacked vertically. Hand-inked linework, expressive faces, subtle cross-hatching, charming domestic comedy, consistent character design.

The same recurring heroine from the reference image appears in all panels. Preserve her recognizable facial identity and hairstyle, rendered naturally as manga ink art.

STORY:
Panel 1: Cozy family living room. The heroine stands beside the television and points toward a small network box on the shelf. Her father enters holding a TV remote, looking puzzled.
Panel 2: The father points the remote at the network box as if trying to change the channel. The heroine turns toward him with a surprised, disbelieving expression.
Panel 3: The TV remains unchanged; the father proudly presses the remote again while the heroine facepalms. Clear visual punchline.

Heroine outfit: elegant dark green blouse translated into black-and-white tonal shading, tailored trousers, delicate earrings. Different pose and camera angle in each panel. Keep the father visually distinct and consistent.
Leave speech balloons empty; no readable text, pseudo-letters, captions, logos or watermark. Exactly three clearly separated horizontal panels, vertical comic page.""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 3. Мама обнаружила, что интернет теперь работает даже на кухне.",
        "prompt": """Create one complete original black-and-white retro manga comic page with EXACTLY THREE horizontal panels stacked vertically. Hand-inked manga artwork, lively expressive faces, clean linework and gentle cross-hatching. Consistent heroine design in all panels.

Use the woman in the reference image as the recurring heroine. Preserve her recognizable facial identity, face shape, eyes, nose, lips and hairstyle, naturally redrawn in manga style.

STORY:
Panel 1: Bright family kitchen in the morning. The heroine enters holding a tablet and notices her mother watching a video smoothly on another device.
Panel 2: The heroine demonstrates the connection on her tablet, smiling and gesturing toward the kitchen. Her mother looks amazed.
Panel 3: The mother happily carries her tablet toward the far corner of the kitchen, while the heroine realizes that the whole family will now expect perfect internet everywhere. Gentle comic punchline.

Heroine outfit: light shirt with rolled sleeves and dark high-waisted trousers, shown with manga tonal shading. Use different natural poses and camera angles across the panels.
Leave speech balloons empty, no letters or pseudo-text, no captions, no logos, no watermark. Exactly three clear horizontal panels on one vertical comic page.""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 4. Младший брат подключил к сети всё, что нашёл в квартире.",
        "prompt": """Create one complete original black-and-white retro manga comic page with EXACTLY THREE horizontal panels stacked vertically. Original hand-inked manga, expressive comedy, crisp linework, detailed cross-hatching, consistent characters.

The recurring heroine is the same woman shown in the reference image. Preserve her recognizable facial identity and hairstyle, redrawn as a manga character in every panel.

STORY:
Panel 1: Slightly chaotic family living room. The younger brother proudly shows the heroine a laptop and tablet connected to the home network.
Panel 2: The brother reveals even more connected objects: a smart speaker, game controller, desk lamp and several other household gadgets. The heroine watches the growing pile with disbelief.
Panel 3: The heroine counts the devices on her fingers, completely overwhelmed, while the brother innocently holds up one last household object to connect. Strong visual punchline.

Heroine outfit: burgundy casual jacket represented with dark manga shading over a simple top and dark trousers. Change pose and camera framing between panels; no static portrait.
Leave speech balloons empty, no readable text, pseudo-letters, captions, logos or watermark. Exactly three clearly separated horizontal panels in a vertical comic page.""",
    },
]


def episode_for_day(day: date) -> dict[str, str]:
    return EPISODES[(day.toordinal() - 1) % len(EPISODES)]
