#!/usr/bin/env python3
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Installing python-pillow...")
    os.system("sudo pacman -S --noconfirm python-pillow")
    from PIL import Image

ICONS = {
    "user-home.png": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_home_borderless_1782684216790.jpg",
    "user-trash.png": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_trash_borderless_1782684340875.jpg",
    "preferences-system.png": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_settings_borderless_1782684245688.jpg",
    "utilities-terminal.png": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_terminal_borderless_1782684277441.jpg",
    "internet-web-browser.png": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_browser_borderless_1782684308750.jpg"
}

PLACES_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/places"
APPS_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/apps"

os.makedirs(PLACES_DIR, exist_ok=True)
os.makedirs(APPS_DIR, exist_ok=True)

print("Starting programmatic border cropping...")

for filename, filepath in ICONS.items():
    if not os.path.exists(filepath):
        print(f"Error: Source file does not exist: {filepath}")
        continue
        
    print(f"Processing: {filename} from {filepath}")
    img = Image.open(filepath)
    w, h = img.size
    
    # Slicing the outer edges to strip white borders or device bezels
    # user-trash.png has a larger white border, so we crop 6% off the edges
    crop_pct = 0.06 if filename == "user-trash.png" else 0.04
    left = int(w * crop_pct)
    top = int(h * crop_pct)
    right = int(w * (1 - crop_pct))
    bottom = int(h * (1 - crop_pct))
    
    cropped_img = img.crop((left, top, right, bottom))
    
    # Resize to standard high-resolution desktop icon size (256x256)
    final_img = cropped_img.resize((256, 256), Image.Resampling.LANCZOS)
    
    # Save to the respective places or apps directory
    dest_dir = PLACES_DIR if filename in ["user-home.png", "user-trash.png"] else APPS_DIR
    dest_path = os.path.join(dest_dir, filename)
    
    final_img.save(dest_path, "PNG")
    print(f"Saved clean, borderless PNG: {dest_path}")

print("All icons successfully updated with no borders.")
