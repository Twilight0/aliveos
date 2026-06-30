#!/usr/bin/env python3
import os
from PIL import Image

ICONS = {
    "accessories-text-editor.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_text_editor_1782684601449.jpg",
        "crop": 0.05
    },
    "utilities-system-monitor.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_monitor_1782684641139.jpg",
        "crop": 0.02
    },
    "system-software-install.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_store_clean_1782684721862.jpg",
        "crop": 0.15
    },
    "multimedia-player.png": {
        "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_media_1782684764797.jpg",
        "crop": 0.15
    }
}

APPS_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/apps"
os.makedirs(APPS_DIR, exist_ok=True)

print("Starting premium icons border cropping...")

for filename, info in ICONS.items():
    filepath = info["src"]
    crop_pct = info["crop"]
    
    if not os.path.exists(filepath):
        print(f"Error: Source file does not exist: {filepath}")
        continue
        
    print(f"Processing: {filename} from {filepath} (crop: {crop_pct})")
    img = Image.open(filepath)
    w, h = img.size
    
    left = int(w * crop_pct)
    top = int(h * crop_pct)
    right = int(w * (1 - crop_pct))
    bottom = int(h * (1 - crop_pct))
    
    cropped_img = img.crop((left, top, right, bottom))
    
    # Resize to standard high-resolution desktop icon size (256x256)
    final_img = cropped_img.resize((256, 256), Image.Resampling.LANCZOS)
    
    dest_path = os.path.join(APPS_DIR, filename)
    final_img.save(dest_path, "PNG")
    print(f"Saved clean, borderless PNG: {dest_path}")

print("Premium icons pack successfully processed.")
