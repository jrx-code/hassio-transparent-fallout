# Home Assistant Transparent Fallout Theme v 1.07

A complete visual overhaul for Home Assistant inspired by the **Fallout** universe (Pip-Boy aesthetic).

This is a **fork** of the [Transparent Blue](https://github.com/JOHLC/transparentblue) theme by JOHLC.

**Repository:** [https://github.com/jrx-code/hassio-transparent-fallout](https://github.com/jrx-code/hassio-transparent-fallout)

## Overview

This project replaces the original blue color palette with phosphor-green (`#14F514`) and radioactive dark backgrounds (`rgba(0, 40, 0, ...)`). It also includes a toolchain (Python) to generate consistent AI artwork for dashboards.

## Preview

<img src="https://raw.githubusercontent.com/jrx-code/hassio-transparent-fallout/main/previews/ha-preview.png" alt="Preview" width="100%">


## 1. Theme Configuration

This theme comes in multiple color variants (YAML files) to match your preferred Pip-Boy HUD color.

### Available Variants

| Theme Name | Filename | Color Code | Description |
| :--- | :--- | :--- | :--- |
| **Transparent Fallout** | `transparent-fallout.yaml` | `#14F514` (Green) | Classic Pip-Boy 3000 aesthetic (Default). |
| **Transparent Fallout Amber** | `transparent-fallout-amber.yaml` | `#FFB641` (Amber) | Fallout: New Vegas Mojave style. |
| **Transparent Fallout Blue** | `transparent-fallout-blue-neon.yaml` | `#08F7FE` (Blue) | Nuka-Cola Quantum / Neon Sci-Fi look. |
| **Transparent Fallout Light** | `transparent-fallout-light.yaml` | High Contrast | Day mode / Terminal printout style. |

### Configuration Details
*   **Fonts:** Configured to match terminal aesthetics (requires system font support or custom CSS injection).
*   **Wallpaper:** Each variant supports its own background image (e.g., `/local/fallout-bg.jpg`, `/local/fallout-blue-neon-bg.jpg`).

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
After installation:
1. Go to your **Profile** (click your user icon in the sidebar bottom left).
2. Under **Theme**, choose your preferred flavor (e.g., **Transparent Fallout Blue Neon**).

## License
MIT License (inherited from upstream).

