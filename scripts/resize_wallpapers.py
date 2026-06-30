#!/usr/bin/env python3
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("PIL/Pillow not found. Installing python-pillow...")
    os.system("sudo pacman -S --noconfirm python-pillow")
    from PIL import Image

WP_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/backgrounds/aliveos"
SOURCE = os.path.join(WP_DIR, "default.png")

RESOLUTIONS = {
    "1920x1080": (1920, 1080),
    "1280x720": (1280, 720),
    "2560x1440": (2560, 1440),
}

if not os.path.exists(SOURCE):
    # Try converting if it's currently saved as .jpg or different casing
    if os.path.exists(SOURCE.replace(".png", ".jpg")):
        SOURCE = SOURCE.replace(".png", ".jpg")
    else:
        print(f"Error: Source image not found at {SOURCE}")
        sys.exit(1)

print(f"Loading source wallpaper: {SOURCE}")
img = Image.open(SOURCE)

for name, size in RESOLUTIONS.items():
    output_path = os.path.join(WP_DIR, f"default_{name}.png")
    print(f"Resizing to {name} ({size[0]}x{size[1]})...")
    # Resizing with high-quality Lanczos filter
    resized_img = img.resize(size, Image.Resampling.LANCZOS)
    resized_img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

print("Wallpaper pack successfully generated.")
