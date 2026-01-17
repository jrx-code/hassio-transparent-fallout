# Home Assistant Transparent Fallout Theme

A complete visual overhaul for Home Assistant inspired by the **Fallout** universe (Pip-Boy aesthetic).

This is a **fork** of the [Transparent Blue](https://github.com/JOHLC/transparentblue) theme by JOHLC.

**Repository:** [https://github.com/jrx-code/hassio-transparent-fallout](https://github.com/jrx-code/hassio-transparent-fallout)

## Overview

This project replaces the original blue color palette with phosphor-green (`#14F514`) and radioactive dark backgrounds (`rgba(0, 40, 0, ...)`). It also includes a toolchain (Python/Bash) to standardize asset management and generate consistent AI artwork for dashboards.

## 1. Theme Configuration
The core file is `transparent-fallout.yaml`.

*   **Primary Color:** Phosphor Green (`#14F514`) - used for active states, text, and icons.
*   **Backgrounds:** Semi-transparent dark green layers optimized for "monitor glow" effects.
*   **Fonts:** Configured to match terminal aesthetics (requires system font support or custom CSS injection).
*   **Wallpaper:** Supports local background injection (default placeholder: `/local/fallout-bg.jpg`).

## 2. Automation Tools
The repository includes scripts to automate the maintenance of dashboard assets.

### Asset Renaming (`rename.sh`)
A Bash script that standardizes Polish filenames to English IDs to ensure consistency across the configuration.
*   **Function:** Maps legacy names (e.g., `kotlownia.png`) to standard IDs (e.g., `boiler-room.png`).
*   **Usage:** `chmod +x rename.sh && ./rename.sh`

### AI Art Prompt Generator (`generate_prompts.py`)
A Python utility for generating Midjourney/DALL-E prompts for new rooms.
*   **Input:** `room-manifest.txt` (list of rooms).
*   **Template:** `prompt.txt` (Fallout-style aesthetic definition).
*   **Output:** `output_prompts.txt` (Ready-to-use prompts).
*   **Usage:** `python3 generate_prompts.py`

## 3. Asset Library
The `assets/` directory (structure flattened in root for this repo) contains rendered graphics for floorplans and rooms.

**Naming Convention:** Kebab-case English (e.g., `server-cabinet.png`, `garage-zs.png`).

| Category | Examples |
| :--- | :--- |
| **Levels** | `level01.png`, `level02.png`, `townhouse.png` |
| **Tech** | `servers.png`, `recuperator.png`, `pv.png` |
| **Living** | `master-bedroom.png`, `kitchen-1.png` |
| **Exterior** | `garage-zs.png`, `gate-01.png` |

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/jrx-code/hassio-transparent-fallout.git
    ```
2.  Copy `transparent-fallout.yaml` to your Home Assistant `themes/` directory.
3.  Add the following to your `configuration.yaml` (if not already present):
    ```yaml
    frontend:
      themes: !include_dir_merge_named themes
    ```
4.  Restart Home Assistant and select **Transparent Fallout** in your profile settings.
5.  (Optional) Run `./rename.sh` if you are migrating graphic assets from a legacy installation.

## License
MIT License (inherited from upstream).

