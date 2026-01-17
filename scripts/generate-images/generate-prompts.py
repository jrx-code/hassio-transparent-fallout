import os
from pathlib import Path

# Configuration
MANIFEST_FILE = "room-manifest.txt"
PROMPT_TEMPLATE_FILE = "prompt.txt"
OUTPUT_FILE = "output_prompts.txt"
PLACEHOLDER = "{ROOM_NAME}"

def clean_room_name(raw_name):
    """
    Converts 'garage-zs.png' or 'master-bedroom' to 'Garage Zs' or 'Master Bedroom'.
    """
    # Remove file extension if present using pathlib
    name = Path(raw_name).stem
    # Replace hyphens/underscores with spaces and apply Title Case
    return name.replace("-", " ").replace("_", " ").title()

def main():
    # 1. Input validation
    if not os.path.exists(MANIFEST_FILE):
        print(f"[ERROR] File '{MANIFEST_FILE}' not found.")
        return
    
    if not os.path.exists(PROMPT_TEMPLATE_FILE):
        print(f"[ERROR] File '{PROMPT_TEMPLATE_FILE}' not found.")
        return

    # 2. Read template
    with open(PROMPT_TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read().strip()
    
    if PLACEHOLDER not in template:
        print(f"[WARNING] Template in '{PROMPT_TEMPLATE_FILE}' does not contain the placeholder '{PLACEHOLDER}'.")

    # 3. Read room list
    rooms = []
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            stripped_line = line.strip()
            # Skip empty lines and lines starting with #
            if stripped_line and not stripped_line.startswith("#"):
                rooms.append(stripped_line)

    print(f"Found {len(rooms)} valid entries in the manifest (comments ignored).")

    # 4. Generate prompts
    generated_prompts = []
    
    for room in rooms:
        human_name = clean_room_name(room)
        # Substitute the placeholder with the cleaned room name
        final_prompt = template.replace(PLACEHOLDER, human_name)
        generated_prompts.append(final_prompt)

    # 5. Save results
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Join prompts with a newline for easy copying
        f.write("\n".join(generated_prompts))

    print(f"[OK] Successfully generated {len(generated_prompts)} prompts in '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()

