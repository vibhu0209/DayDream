 # Daydream Game

**Daydream Game** is an interactive Ren’Py visual novel blending Indian folklore, heartfelt choices, and surreal adventure. The project leverages the Ren’Py engine (8.4.1), modern Python logic, and assets generated or enhanced through open source libraries and advanced AI systems.

---

### Features

- **Genre:** Narrative adventure, interactive fiction, fantasy realism
- **Engine:** Ren’Py 8.4.1 (Visual Novel framework)
- **Platforms:** Windows, Linux, macOS (cross-platform via Ren’Py launcher)
- **Language:** English + supports translation via `game/tl`
- **Status:** Playable (v1.0)

---

## How AI is Used

- **AI Error Resolution:** The game’s Ren’Py code was debugged and refactored with the help of advanced AI, ensuring 0 errors related to deprecated engine internals.  
- **AI Story Generation:** Character arcs, story structure, events, and dialogue options were conceptualized with the aid of AI text-generation models, ensuring cohesive worldbuilding and rich player choice.  
- **Asset Generation:** Sprite art, background images, and audio cues were created or enhanced using AI image generators (e.g., open-source Stable Diffusion, Adobe Firefly) and AI music tools.  
- **Open Source Integration:** Music, SFX, and some images utilize assets from open-source libraries, curated and remixed using AI for seamless style and tone.

---

## Installation

1. **Download & Extract:** Place all project files in the `game` folder of your Ren’Py project.
2. **Assets:** Ensure the subfolders contain the following:
    - `game/images/` — All character and background images (PNG/JPG).
    - `game/audio/` — All music (.ogg/.mp3) and sound effects (.wav/.mp3).
    - `game/gui/` — Dialogue boxes, menus, icons (PNG, SVG).
    - `game/tl/` — Localization files (optional).
    - `game/libs/` — Any Python modules or custom extensions.
3. **Run:** Open the project in Ren’Py Launcher and click "Launch Project".

---

## Assets & Attributions

### Images

- **Character artwork:** Generated using Stable Diffusion (AI), Adobe Firefly, and curated via open-source image sets (CC-BY-SA 4.0 where applicable).
- **Backgrounds:** A mix of open-source CC0 images and generative art (Adobe Firefly), post-processed for style consistency.

### Audio

- **Music:** Royalty-free base tracks sourced from OpenGameArt.org, remixed/re-synthesized via AI tools (e.g., musif, Sync Toolbox).
- **Sound Effects:** Sourced via open-source libraries and Adobe tools, some generated from AI audio synthesis models.

### GUI & Visual Elements

- **Menus, Icons:** Adobe Illustrator/Firefly assets (customized), OpenGameArt and Ren’Py GUI customization guides.

---

## Open Source Libraries Used

- **Ren’Py Engine:** Main interactive novel framework.
- **musif, Sync Toolbox:** For music analysis and AI-powered soundtrack remixing.
- **Stable Diffusion / Community Models:** AI image generation for sprites/backgrounds.
- **Adobe Firefly:** AI-enhanced visual and music asset generation.
- **CC0/CC-BY Libraries:** OpenGameArt.org (music/SFX/images), Unsplash, Pixabay (backgrounds).

---

## Troubleshooting

- **No deprecated function errors:** All code is modernized for Ren’Py 8.4.1+; do not copy over engine files from older releases.
- **Missing assets:** Ensure all image and audio files referenced in script.rpy are present with matching filenames.
- **.rpyc and cache:** If upgrading, delete all .rpyc files in `game/` and clear `game/cache/` before launching.

---

## Credits

- **Story & Code:** Generated and curated with Perplexity AI/ChatGPT guidance.
- **Artwork:** Stable Diffusion community, Adobe Firefly AI, OpenGameArt artists.
- **Music & SFX:** Open source remixing (musif), AI-generated cues, editing in Audacity and
