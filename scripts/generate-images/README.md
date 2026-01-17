# Fallout Home Assistant Theme & Assets

## Overview
This repository contains a complete graphic overhaul for a Home Assistant dashboard inspired by the **Fallout** universe (Pip-Boy aesthetic). It includes a custom YAML theme, a standardized library of room renders/icons, and automation scripts for asset management.

## Project Contents

### 1. Themes
*   **`transparent-fallout.yaml`**
    A custom Home Assistant theme based on the *Transparent Blue* theme.
    *   **Aesthetic:** Phosphor Green (`#14F514`) text and active elements against dark, radioactive green backgrounds.
    *   **Features:** Semi-transparent cards, terminal-style fonts settings, and integration with local background images (e.g., `fallout-bg.jpg`).

### 2. Automation Scripts
Tools designed to standardize asset filenames and generate AI art prompts.

*   **`generate_prompts.py`** (Python)
    *   Reads a list of rooms from `room-manifest.txt`.
    *   Injects room names into a predefined Fallout-style Midjourney/DALL-E prompt template (`prompt.txt`).
    *   Outputs ready-to-use prompts to `output_prompts.txt`.
    *   *Usage:* `python3 generate_prompts.py`

*   **`rename.sh`** (Bash)
    *   Batch renames original legacy filenames (Polish) to standardized English IDs (e.g., `kotlownia.png` -> `boiler-room.png`).
    *   Prevents overwriting existing files with collision checks.
    *   *Usage:* `chmod +x rename.sh && ./rename.sh`

### 3. Configuration Files
*   **`room-manifest.txt`**
    Input list of filenames or room IDs for the Python generator script. Supports comments (lines starting with `#`).
*   **`prompt.txt`**
    Template file containing the "master prompt" for the AI generator. Contains a `{ROOM_NAME}` placeholder.

### 4. Graphic Assets
A library of PNG images used for dashboard cards, floorplans, and area representations.

#### Naming Convention
Files follow a strict `kebab-case` English naming convention (e.g., `server-cabinet.png`, `garage-zs.png`).

#### Asset Categories
*   **Levels:** Floorplans (`level01.png`, `level02.png`), external views (`townhouse.png`).
*   **Living Spaces:** Bedrooms, Kitchens, Living rooms (`master-bedroom.png`, `kitchen-1.png`).
*   **Technical:** Server infrastructure, HVAC, PV systems (`servers.png`, `recuperator.png`).
*   **Exterior:** Garages, Gates, Garden (`garage-zs.png`, `gate-01.png`).

---

## Quick Start

1.  **Install Theme:** Copy `transparent-fallout.yaml` to your HA `themes/` folder and reload themes.
2.  **Standardize Assets:** Run `./rename.sh` to align your file naming.
3.  **Generate New Art:**
    *   List your missing rooms in `room-manifest.txt`.
    *   Run `python3 generate_prompts.py`.
    *   Paste the output into Midjourney/DALL-E to get matching visuals.

