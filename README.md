# Home Assistant Transparent Fallout Theme v 1.07

A complete visual overhaul for Home Assistant inspired by the **Fallout** universe (Pip-Boy aesthetic).

This is a **fork** of the [Transparent Blue](https://github.com/JOHLC/transparentblue) theme by JOHLC.

**Repository:** [https://github.com/jrx-code/hassio-transparent-fallout](https://github.com/jrx-code/hassio-transparent-fallout)

## Overview

This project replaces the original blue color palette with phosphor-green (`#14F514`) and radioactive dark backgrounds (`rgba(0, 40, 0, ...)`). It also includes a toolchain (Python) to generate consistent AI artwork for dashboards.

![Transparent Fallout Preview]()

## Preview

<img src="https://raw.githubusercontent.com/jrx-code/hassio-transparent-fallout/1.0.7/ha-preview.png" alt="Preview" width="100%">


## 1. Theme Configuration
The core file is `transparent-fallout.yaml`.

*   **Primary Color:** Phosphor Green (`#14F514`) - used for active states, text, and icons.
*   **Backgrounds:** Semi-transparent dark green layers optimized for "monitor glow" effects.
*   **Fonts:** Configured to match terminal aesthetics (requires system font support or custom CSS injection).
*   **Wallpaper:** Supports local background injection (default placeholder: `/local/fallout-bg.jpg`).

## 2. Automation Tools
The repository includes scripts to automate the maintenance of dashboard assets.

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

### Option 1: HACS (Recommended)
This is a custom repository, so you need to add it manually to HACS.

1. Open **HACS** in Home Assistant.
2. Go to **Frontend**.
3. Click the **3 dots** in the top right corner and select **Custom repositories**.
4. Paste the repository URL:  
   `https://github.com/jrx-code/hassio-transparent-fallout`
5. Select category: **Theme**.
6. Click **Add**.
7. Now search for **Transparent Fallout** in the HACS Frontend tab and install it.
8. Restart Home Assistant.

### Option 2: Manual (Git Clone)
For advanced users or contributors.

1. Go to your Home Assistant `themes` directory:
    ```bash
    cd /config/themes/
    ```
2. Clone the repository:
    ```bash
    git clone https://github.com/jrx-code/hassio-transparent-fallout.git transparent-fallout
    ```
3. Add the following to your `configuration.yaml` (if not already present):
    ```yaml
    frontend:
      themes: !include_dir_merge_named themes
    ```
4. Restart Home Assistant.

### Activation
After installation (via HACS or Manual):
1. Go to your **Profile** (click your user icon in the sidebar bottom left).
2. Under **Theme**, select **Transparent Fallout**.

## License
MIT License (inherited from upstream).

