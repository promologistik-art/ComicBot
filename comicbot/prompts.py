from __future__ import annotations

from datetime import date


# Первый сезон: короткие самостоятельные трёхпанельные эпизоды
# одной семейной истории. Постоянная героиня — фотографический identity reference.
# Визуальный стиль: фотореалистичный кинематографический фотокомикс.
# Не иллюстрация и не манга: каждая панель выглядит как кадр игрового фильма.
GLOBAL_STYLE = """VISUAL STYLE — ABSOLUTE PRIORITY:
Create a PHOTOREALISTIC LIVE-ACTION CINEMATIC PHOTO COMIC, not an illustration.
Every panel must look like a real high-end movie still photographed with a real
camera and real human actors. Natural human skin texture with visible fine detail,
realistic eyes, realistic hair strands, physically accurate clothing and materials,
natural proportions, cinematic practical lighting, believable depth of field,
professional photography, subtle film color grading.

HEROINE IDENTITY — CRITICAL:
Use the supplied reference photograph as the exact identity reference for the adult
woman. She must look like the same real photographed woman in every panel:
preserve her facial identity, face shape, eyes, eyebrows, nose, lips, cheekbones,
jawline, skin tone and distinctive chestnut-brown hair. Do not reinterpret,
beautify into a different person, stylize, redraw or approximate her face.
Keep her appearance photographic and lifelike. Clothing, pose, expression,
camera angle and environment may change; her identity must not.

COMIC PAGE LAYOUT:
One complete vertical comic page with EXACTLY THREE wide horizontal panels stacked
top to bottom. Clearly visible clean panel borders and gutters. Each panel is a
separate cinematic photograph from the same live-action story. Include simple
empty white speech balloons with clean black outlines, positioned so they do not
cover faces. Leave all balloons completely blank: absolutely no letters, words,
symbols or pseudo-text. Consistent photographic realism across all panels.

STRICTLY AVOID:
manga, anime, cartoon, comic-book illustration, hand-drawn art, ink drawing,
sketch, line art, cel shading, cross-hatching, painted appearance, 3D render,
plastic skin, doll-like face, exaggerated eyes, altered facial identity.
"""


EPISODES = [
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 1. В доме появился загадочный ящик. И, кажется, он уже подключён ко всему.",
        "prompt": GLOBAL_STYLE + """
STORY — "The mysterious box":
Panel 1: In a cozy modern family apartment at evening, the heroine notices a
mysterious small black network box on a shelf. She pauses mid-step and looks at
it suspiciously. Medium-wide cinematic shot.
Panel 2: Photographic close-up: she leans closer and carefully reaches one finger
toward the strange box; a tiny indicator light glows. Her expression changes from
curiosity to concern. Keep her real face clearly recognizable.
Panel 3: Wider live-action shot: several household devices around the room suddenly
light up at once. The heroine stands in the middle of the room, startled, holding
her hands up in disbelief. Clear visual punchline.

Heroine outfit: soft oversized cream cardigan, dark fitted jeans, simple jewelry.
Vary her pose and camera framing naturally between panels. The whole page must
look like three stills from one photorealistic comedy film.
No captions, logos, watermarks or readable text. Entire page visible in a vertical
composition.
""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 2. Папа решил, что загадочный ящик — это новый пульт от телевизора.",
        "prompt": GLOBAL_STYLE + """
STORY:
Panel 1: Cozy family living room. The heroine stands beside the television and
points toward a small network box on the shelf. Her father enters holding a TV
remote, looking puzzled. Photorealistic medium shot.
Panel 2: The father points the remote at the network box as if trying to change
the channel. The heroine turns toward him with a surprised, disbelieving expression.
Cinematic over-the-shoulder composition.
Panel 3: The TV remains unchanged; the father proudly presses the remote again
while the heroine facepalms. Clear visual punchline, natural live-action expressions.

Heroine outfit: elegant dark green blouse, tailored trousers, delicate earrings.
Different natural poses and camera angles in each panel. Keep the father visually
distinct and consistent. Photographic skin and hair detail throughout.
No captions, logos, watermarks or readable text. Exactly three bordered panels.
""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 3. Мама обнаружила, что интернет теперь работает даже на кухне.",
        "prompt": GLOBAL_STYLE + """
STORY:
Panel 1: Bright family kitchen in the morning. The heroine enters holding a tablet
and notices her mother watching a video smoothly on another device. Natural
daylight, cinematic wide shot.
Panel 2: The heroine demonstrates the connection on her tablet, smiling and
gesturing toward the kitchen. Her mother looks amazed. Realistic two-shot.
Panel 3: The mother happily carries her tablet toward the far corner of the
kitchen, while the heroine realizes that the whole family will now expect perfect
internet everywhere. Gentle visual punchline.

Heroine outfit: light shirt with rolled sleeves and dark high-waisted trousers.
Use different natural poses and camera angles across the panels. Keep all people
photorealistic, with natural expressions and realistic proportions.
No captions, logos, watermarks or readable text. Three clear horizontal panels.
""",
    },
    {
        "title": "Ящик Пандоры — семейный VPN",
        "caption": "Семейный VPN · Глава 4. Младший брат подключил к сети всё, что нашёл в квартире.",
        "prompt": GLOBAL_STYLE + """
STORY:
Panel 1: Slightly chaotic family living room. The heroine sits beside her younger
brother, who proudly shows her a laptop and tablet connected to the home network.
Photorealistic medium shot.
Panel 2: The brother reveals even more connected objects: a smart speaker, game
controller, desk lamp and several other household gadgets. The heroine watches
the growing pile with disbelief. Lively but believable cinematic composition.
Panel 3: The heroine counts the devices on her fingers, completely overwhelmed,
while the brother innocently holds up one last household object to connect.
Strong visual punchline.

Heroine outfit: burgundy casual leather jacket over a simple top and dark trousers.
Change pose and camera framing between panels. Natural human faces and hands.
No captions, logos, watermarks or readable text. Exactly three clear horizontal
panels in one vertical photorealistic page.
""",
    },
]


def episode_for_day(day: date) -> dict[str, str]:
    return EPISODES[(day.toordinal() - 1) % len(EPISODES)]
