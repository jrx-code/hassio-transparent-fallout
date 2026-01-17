# Home Assistant Transparent Fallout Theme v1.1.2

A complete visual overhaul for Home Assistant inspired by the **Fallout** universe (Pip-Boy aesthetic).

This is a **fork** of the [Transparent Blue](https://github.com/JOHLC/transparentblue) theme by JOHLC.

**Repository:** [https://github.com/jrx-code/hassio-transparent-fallout](https://github.com/jrx-code/hassio-transparent-fallout)

## Preview

| Default (Green) |
|:---:|
| <img src="https://raw.githubusercontent.com/jrx-code/hassio-transparent-fallout/main/previews/ha-preview-default.png" alt="Default Green Theme" width="100%"> |

| Amber | Blue | Light |
|:---:|:---:|:---:|
| <img src="https://raw.githubusercontent.com/jrx-code/hassio-transparent-fallout/main/previews/ha-preview-amber.png" alt="Amber Theme" width="100%"> | <img src="https://raw.githubusercontent.com/jrx-code/hassio-transparent-fallout/main/previews/ha-preview-blue.png" alt="Blue Theme" width="100%"> | <img src="https://raw.githubusercontent.com/jrx-code/hassio-transparent-fallout/main/previews/ha-preview-light.png" alt="Light Theme" width="100%"> |

## Overview

This project offers **four Fallout-inspired theme variants** for Home Assistant, each with unique color palettes and atmospheric backgrounds. All themes feature semi-transparent dark backgrounds optimized for "monitor glow" effects and support custom wallpapers. The repository also includes a Python toolchain for generating consistent AI artwork for dashboards.

### Available Themes

- **Default (Green)** - Classic Pip-Boy phosphor green (`#14F514`)
- **Amber** - Warm amber/sepia tones (`#FFB641`) for a vintage CRT monitor feel
- **Blue** - Neon cyan (`#00D4FF`) inspired by Nuka-Cola Quantum
- **Light** - Experimental light mode variant with customizable icon colors

## 1. Theme Configuration

### Transparent Fallout (Default - Green)
**File:** `transparent-fallout.yaml`

Classic Pip-Boy aesthetic with phosphor green display.

*   **Primary Color:** Phosphor Green (`#14F514`) - used for active states, text, and icons.
*   **Backgrounds:** Semi-transparent dark green layers (`rgba(0, 40, 0, ...)`) optimized for "monitor glow" effects.
*   **Fonts:** Configured to match terminal aesthetics (requires system font support or custom CSS injection).
*   **Wallpaper:** Supports local background injection (default placeholder: `/local/fallout-bg.jpg`).

### Transparent Fallout Amber
**File:** `transparent-fallout-amber.yaml`

Warm amber/sepia theme resembling vintage CRT monitors or candlelight terminals.

*   **Primary Color:** Phosphor Amber (`#FFB641`) - warm amber for all active elements.
*   **Backgrounds:** Semi-transparent dark brown/sepia layers (`rgba(45, 25, 0, ...)`) creating a warm glow.
*   **Wallpaper:** `/local/fallout-amber-bg.jpg`

### Transparent Fallout Blue
**File:** `transparent-fallout-blue.yaml`

Neon cyan theme inspired by Nuka-Cola Quantum and sci-fi terminals.

*   **Primary Color:** Neon Blue (`#00D4FF`) - bright cyan for futuristic aesthetic.
*   **Backgrounds:** Semi-transparent dark blue layers (`rgba(0, 25, 40, ...)`) with cool tones.
*   **Wallpaper:** `/local/fallout-blue-bg.jpg`

### Transparent Fallout Light
**File:** `transparent-fallout-light.yaml`

Experimental light mode variant with extensive customization options.

*   **Icon Color:** Customizable (default: `#bdddcb`)
*   **Backgrounds:** Dark semi-transparent layers
*   **Note:** Work in progress - may have visual inconsistencies.

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
2. Under **Theme**, select one of:
   - **Transparent Fallout** (green)
   - **Transparent Fallout Amber**
   - **Transparent Fallout Blue**
   - **Transparent Fallout Light**

## Background Images

Each theme expects a corresponding background image in `/config/www/`:

- `/local/fallout-bg.jpg` - Default green theme
- `/local/fallout-amber-bg.jpg` - Amber theme
- `/local/fallout-blue-bg.jpg` - Blue theme

You can use any Fallout-themed wallpaper or generate your own using AI tools (Midjourney, DALL-E, Stable Diffusion).

## Changelog

### v1.1.2 (2026-01-17)
- Added **Amber** theme variant (`transparent-fallout-amber.yaml`)
- Added **Blue** theme variant (`transparent-fallout-blue.yaml`)
- Updated **Light** theme with customizable icon colors (`#bdddcb`)
- Fixed YAML indentation issues across all themes
- Added preview images for all theme variants in `previews/` directory
- Updated README with comprehensive theme descriptions

### v1.0.7
- Initial public release
- Classic green Pip-Boy theme
- Python automation tools for AI art generation

## License
MIT License (inherited from upstream).

