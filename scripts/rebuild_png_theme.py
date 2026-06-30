#!/usr/bin/env python3
import os
import shutil
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Installing python-pillow...")
    os.system("sudo pacman -S --noconfirm python-pillow")
    from PIL import Image

THEME_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos"

# 1. Source configuration (JPEG sources from artifacts with their crop percentages)
ICONS_CONFIG = {
    "user-home.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_home_borderless_1782684216790.jpg",
        "crop": 0.05,
        "category": "places"
    },
    "user-trash.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_trash_borderless_1782684340875.jpg",
        "crop": 0.06,
        "category": "places"
    },
    "preferences-system.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_settings_borderless_1782684245688.jpg",
        "crop": 0.02,
        "category": "apps"
    },
    "utilities-terminal.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_terminal_borderless_1782684277441.jpg",
        "crop": 0.02,
        "category": "apps"
    },
    "internet-web-browser.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_browser_borderless_1782684308750.jpg",
        "crop": 0.12,
        "category": "apps"
    },
    "accessories-text-editor.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_text_editor_1782684601449.jpg",
        "crop": 0.05,
        "category": "apps"
    },
    "multimedia-player.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_media_1782684764797.jpg",
        "crop": 0.15,
        "category": "apps"
    },
    "utilities-system-monitor.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_monitor_1782684641139.jpg",
        "crop": 0.02,
        "category": "apps"
    },
    "system-software-install.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_store_clean_1782684721862.jpg",
        "crop": 0.15,
        "category": "apps"
    },
    "network-wireless.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_network_1782685087608.jpg",
        "crop": 0.15,
        "category": "apps"
    },
    "audio-volume-high.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_audio_1782685127179.jpg",
        "crop": 0.20,
        "category": "apps"
    },
    "x-office-document.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_office_1782685172145.jpg",
        "crop": 0.05,
        "category": "apps"
    }
}

SIZES = [16, 22, 32, 48, 64, 128, 256]

# 2. Clean out the old theme folder completely
print("=== Re-initializing AliveOS Icon Theme ===")
if os.path.exists(THEME_DIR):
    shutil.rmtree(THEME_DIR)
    print(f"Deleted old icon theme directory: {THEME_DIR}")

# 3. Create clean layout folders
for size in SIZES:
    os.makedirs(os.path.join(THEME_DIR, f"{size}x{size}", "apps"), exist_ok=True)
    os.makedirs(os.path.join(THEME_DIR, f"{size}x{size}", "places"), exist_ok=True)
print("Created theme folder hierarchies for sizes: 16, 22, 32, 48, 64, 128, 256.")

# 4. Process and resize PNGs (keeping the original solid background)
print("\n=== Generating PNG Icons ===")
for filename, info in ICONS_CONFIG.items():
    src_path = info["src"]
    crop_pct = info["crop"]
    category = info["category"]
    
    if not os.path.exists(src_path):
        print(f"Error: Source file not found: {src_path}")
        continue
        
    # Open the image in RGB mode (preserving solid dark backgrounds)
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    
    # Crop borders according to the spec
    left = int(w * crop_pct)
    top = int(h * crop_pct)
    right = int(w * (1 - crop_pct))
    bottom = int(h * (1 - crop_pct))
    cropped = img.crop((left, top, right, bottom))
    
    # Save for each common size
    for size in SIZES:
        resized = cropped.resize((size, size), Image.Resampling.LANCZOS)
        dest_path = os.path.join(THEME_DIR, f"{size}x{size}", category, filename)
        resized.save(dest_path, "PNG")
        
    print(f"Processed and generated: {filename} (all sizes)")

# 5. Populate generic folder.png icon inside places
print("\n=== Creating Folder.png copies ===")
for size in SIZES:
    home_path = os.path.join(THEME_DIR, f"{size}x{size}", "places", "user-home.png")
    folder_path = os.path.join(THEME_DIR, f"{size}x{size}", "places", "folder.png")
    if os.path.exists(home_path):
        shutil.copy2(home_path, folder_path)

# 6. Generate index.theme
index_theme_content = """[Icon Theme]
Name=AliveOS
Comment=Custom neon dark square icon theme for AliveOS
Inherits=Papirus-Dark,Adwaita,hicolor
Directories=16x16/apps,16x16/places,22x22/apps,22x22/places,32x32/apps,32x32/places,48x48/apps,48x48/places,64x64/apps,64x64/places,128x128/apps,128x128/places,256x256/apps,256x256/places

[16x16/apps]
Size=16
Context=Applications
Type=Fixed

[16x16/places]
Size=16
Context=Places
Type=Fixed

[22x22/apps]
Size=22
Context=Applications
Type=Fixed

[22x22/places]
Size=22
Context=Places
Type=Fixed

[32x32/apps]
Size=32
Context=Applications
Type=Fixed

[32x32/places]
Size=32
Context=Places
Type=Fixed

[48x48/apps]
Size=48
Context=Applications
Type=Fixed

[48x48/places]
Size=48
Context=Places
Type=Fixed

[64x64/apps]
Size=64
Context=Applications
Type=Fixed

[64x64/places]
Size=64
Context=Places
Type=Fixed

[128x128/apps]
Size=128
Context=Applications
Type=Fixed

[128x128/places]
Size=128
Context=Places
Type=Fixed

[256x256/apps]
Size=256
Context=Applications
Type=Fixed

[256x256/places]
Size=256
Context=Places
Type=Fixed
"""

index_path = os.path.join(THEME_DIR, "index.theme")
with open(index_path, "w") as f:
    f.write(index_theme_content)
print(f"\nCreated theme definition: {index_path}")

print("\n=== Rebuild Complete ===")
