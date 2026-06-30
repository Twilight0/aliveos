#!/usr/bin/env python3
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Installing python-pillow...")
    os.system("sudo pacman -S --noconfirm python-pillow")
    from PIL import Image

ICONS_CONFIG = {
    "user-home.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_home_borderless_1782684216790.jpg",
        "crop": 0.05,
        "type": "places"
    },
    "user-trash.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_trash_borderless_1782684340875.jpg",
        "crop": 0.06,
        "type": "places"
    },
    "preferences-system.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_settings_borderless_1782684245688.jpg",
        "crop": 0.02,
        "type": "apps"
    },
    "utilities-terminal.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_terminal_borderless_1782684277441.jpg",
        "crop": 0.02,
        "type": "apps"
    },
    "internet-web-browser.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_browser_borderless_1782684308750.jpg",
        "crop": 0.12,
        "type": "apps"
    },
    "accessories-text-editor.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_text_editor_1782684601449.jpg",
        "crop": 0.05,
        "type": "apps"
    },
    "multimedia-player.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_media_1782684764797.jpg",
        "crop": 0.15,
        "type": "apps"
    },
    "utilities-system-monitor.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_monitor_1782684641139.jpg",
        "crop": 0.02,
        "type": "apps"
    },
    "system-software-install.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_store_clean_1782684721862.jpg",
        "crop": 0.15,
        "type": "apps"
    },
    "network-wireless.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_network_1782685087608.jpg",
        "crop": 0.15,
        "type": "apps"
    },
    "audio-volume-high.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_audio_1782685127179.jpg",
        "crop": 0.20,
        "type": "apps"
    },
    "x-office-document.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_office_1782685172145.jpg",
        "crop": 0.05,
        "type": "apps"
    }
}

PLACES_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/places/48"
APPS_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/apps/scalable"

# Ensure directories exist
os.makedirs(PLACES_DIR, exist_ok=True)
os.makedirs(APPS_DIR, exist_ok=True)

# Clean up old places/ and apps/ folders from the root of the icon theme to avoid confusion
old_places = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/places"
old_apps = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/apps"
for old_dir in [old_places, old_apps]:
    if os.path.exists(old_dir) and not old_dir.endswith("/48") and not old_dir.endswith("/scalable"):
        # We need to be careful: since places/48 is inside places/, we shouldn't delete the parent recursively if it contains child folders we want
        # Let's delete the files inside places/ and apps/ but NOT the folders places/48, places/16, apps/scalable
        for item in os.listdir(old_dir):
            item_path = os.path.join(old_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"Removed old parent-level file: {item_path}")

print("=== Starting Black-Keying & Transparent PNG Generation ===")

for filename, info in ICONS_CONFIG.items():
    src_path = info["src"]
    crop_pct = info["crop"]
    category = info["type"]
    
    if not os.path.exists(src_path):
        print(f"Error: Source file not found: {src_path}")
        continue
        
    print(f"Processing: {filename} with crop {crop_pct}...")
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size
    
    # 1. Crop the border edges
    left = int(w * crop_pct)
    top = int(h * crop_pct)
    right = int(w * (1 - crop_pct))
    bottom = int(h * (1 - crop_pct))
    cropped = img.crop((left, top, right, bottom))
    
    # 2. Key out black background to transparency (luminance keying)
    # We load pixel data
    pixels = cropped.load()
    cw, ch = cropped.size
    
    for y in range(ch):
        for x in range(cw):
            r, g, b, a = pixels[x, y]
            
            # Brightness value represents how glowing the pixel is
            brightness = max(r, g, b)
            
            if brightness < 12:
                # Near-black pixels become fully transparent
                pixels[x, y] = (0, 0, 0, 0)
            else:
                # Alpha is proportional to brightness
                alpha = brightness
                
                # Unpremultiply: normalize colors by dividing by the alpha factor to keep colors vibrant
                new_r = min(255, int(r * 255 / alpha))
                new_g = min(255, int(g * 255 / alpha))
                new_b = min(255, int(b * 255 / alpha))
                
                pixels[x, y] = (new_r, new_g, new_b, alpha)
                
    # 3. Resize to 256x256
    resized = cropped.resize((256, 256), Image.Resampling.LANCZOS)
    
    # 4. Save to destination
    dest_dir = PLACES_DIR if category == "places" else APPS_DIR
    dest_path = os.path.join(dest_dir, filename)
    
    # Remove existing file if it exists
    if os.path.exists(dest_path):
        os.remove(dest_path)
        
    resized.save(dest_path, "PNG")
    print(f"Saved transparent PNG: {dest_path}")

# 5. Overwrite folder.png and other duplicates
print("\n=== Copying base icons to duplicate names ===")
sh = os.path.join(PLACES_DIR, "user-home.png")
sh_dest = os.path.join(PLACES_DIR, "folder.png")
if os.path.exists(sh):
    if os.path.exists(sh_dest):
        os.remove(sh_dest)
    os.system(f"cp {sh} {sh_dest}")
    print(f"Copied folder icon: {sh_dest}")

# 6. Delete the matching SVG versions of these files to avoid system overrides
print("\n=== Deleting original SVG overrides to force PNG use ===")
SVG_DELETES = [
    # places
    "places/48/user-home.svg",
    "places/48/user-trash.svg",
    "places/48/user-trash-full.svg",
    "places/48/folder-home.svg",
    "places/48/folder-trash.svg",
    "places/48/folder.svg",
    # apps
    "apps/scalable/preferences-system.svg",
    "apps/scalable/utilities-terminal.svg",
    "apps/scalable/internet-web-browser.svg",
    "apps/scalable/accessories-text-editor.svg",
    "apps/scalable/multimedia-player.svg",
    "apps/scalable/utilities-system-monitor.svg",
    "apps/scalable/system-software-install.svg",
    "apps/scalable/network-wireless.svg",
    "apps/scalable/audio-volume-high.svg",
    "apps/scalable/x-office-document.svg",
    # also some common names
    "apps/scalable/firefox.svg",
    "apps/scalable/Alacritty.svg",
    "apps/scalable/vlc.svg",
    "apps/scalable/mpv.svg",
    "apps/scalable/htop.svg",
    "apps/scalable/code.svg"
]

THEME_BASE = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos"
for relative_path in SVG_DELETES:
    target_svg = os.path.join(THEME_BASE, relative_path)
    if os.path.exists(target_svg):
        os.remove(target_svg)
        print(f"Deleted original SVG: {target_svg}")

print("\nAll transparent, borderless icons are ready and integrated into the BeautyLine folder layout.")
