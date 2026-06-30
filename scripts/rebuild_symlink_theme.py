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

# 1. Source configuration
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

# 2. File duplication mappings
COPY_MAPPINGS = {
    "places": {
        "folder.png": "user-home.png",
        "folder-remote.png": "user-home.png",
        "folder-home.png": "user-home.png",
        "folder-custom.png": "user-home.png",
        "user-desktop.png": "user-home.png",
        "folder-documents.png": "user-home.png",
        "folder-downloads.png": "user-home.png",
        "folder-music.png": "user-home.png",
        "folder-pictures.png": "user-home.png",
        "folder-videos.png": "user-home.png",
        "folder-templates.png": "user-home.png",
        "folder-publicshare.png": "user-home.png",
        "user-trash-empty.png": "user-trash.png",
        "user-trash-full.png": "user-trash.png",
        "user-trash-empty-state.png": "user-trash.png",
        "user-trash-full-state.png": "user-trash.png"
    },
    "apps": {
        "cinnamon-control-center.png": "preferences-system.png",
        "gnome-control-center.png": "preferences-system.png",
        "settings.png": "preferences-system.png",
        "preferences-desktop.png": "preferences-system.png",
        "preferences-system-details.png": "preferences-system.png",
        "system-settings.png": "preferences-system.png",
        "control-panel.png": "preferences-system.png",
        "terminal.png": "utilities-terminal.png",
        "gnome-terminal.png": "utilities-terminal.png",
        "kitty.png": "utilities-terminal.png",
        "alacritty.png": "utilities-terminal.png",
        "xterm.png": "utilities-terminal.png",
        "konsole.png": "utilities-terminal.png",
        "utilities-terminal-alt.png": "utilities-terminal.png",
        "web-browser.png": "internet-web-browser.png",
        "firefox.png": "internet-web-browser.png",
        "google-chrome.png": "internet-web-browser.png",
        "chromium.png": "internet-web-browser.png",
        "opera.png": "internet-web-browser.png",
        "brave-browser.png": "internet-web-browser.png",
        "vivaldi.png": "internet-web-browser.png",
        "epiphany.png": "internet-web-browser.png",
        "midori.png": "internet-web-browser.png",
        "text-editor.png": "accessories-text-editor.png",
        "gedit.png": "accessories-text-editor.png",
        "kate.png": "accessories-text-editor.png",
        "mousepad.png": "accessories-text-editor.png",
        "pluma.png": "accessories-text-editor.png",
        "leafpad.png": "accessories-text-editor.png",
        "sublime-text.png": "accessories-text-editor.png",
        "code.png": "accessories-text-editor.png",
        "visual-studio-code.png": "accessories-text-editor.png",
        "vscode.png": "accessories-text-editor.png",
        "media-player.png": "multimedia-player.png",
        "vlc.png": "multimedia-player.png",
        "mpv.png": "multimedia-player.png",
        "totem.png": "multimedia-player.png",
        "rhythmbox.png": "multimedia-player.png",
        "clementine.png": "multimedia-player.png",
        "spotify.png": "multimedia-player.png",
        "celluloid.png": "multimedia-player.png",
        "audio-player.png": "multimedia-player.png",
        "video-player.png": "multimedia-player.png",
        "system-monitor.png": "utilities-system-monitor.png",
        "gnome-system-monitor.png": "utilities-system-monitor.png",
        "htop.png": "utilities-system-monitor.png",
        "btop.png": "utilities-system-monitor.png",
        "top.png": "utilities-system-monitor.png",
        "software-center.png": "system-software-install.png",
        "pamac-manager.png": "system-software-install.png",
        "discover.png": "system-software-install.png",
        "gourmet.png": "system-software-install.png",
        "synaptic.png": "system-software-install.png",
        "package-manager.png": "system-software-install.png",
        "network.png": "network-wireless.png",
        "network-wired.png": "network-wireless.png",
        "network-wireless-connected.png": "network-wireless.png",
        "network-workgroup.png": "network-wireless.png",
        "network-server.png": "network-wireless.png",
        "audio-volume-medium.png": "audio-volume-high.png",
        "audio-volume-low.png": "audio-volume-high.png",
        "audio-volume-muted.png": "audio-volume-high.png",
        "audio-card.png": "audio-volume-high.png",
        "volume.png": "audio-volume-high.png",
        "sound.png": "audio-volume-high.png",
        "office.png": "x-office-document.png",
        "libreoffice-writer.png": "x-office-document.png",
        "libreoffice.png": "x-office-document.png",
        "document.png": "x-office-document.png",
        "wps-office-wps.png": "x-office-document.png"
    }
}

SIZES = [16, 22, 32, 48, 64, 128, 256]

# 3. Clean out target directory completely
print("=== Rebuilding Standalone Icon Theme with Symlinks ===")
if os.path.exists(THEME_DIR):
    shutil.rmtree(THEME_DIR)
    print(f"Deleted old icon theme directory: {THEME_DIR}")

# 4. Create directories
for size in SIZES:
    os.makedirs(os.path.join(THEME_DIR, f"{size}x{size}", "apps"), exist_ok=True)
    os.makedirs(os.path.join(THEME_DIR, f"{size}x{size}", "places"), exist_ok=True)

# 5. Compile core icons
print("\n=== Compiling Core PNG Icons ===")
for filename, info in ICONS_CONFIG.items():
    src_path = info["src"]
    crop_pct = info["crop"]
    category = info["category"]
    
    if not os.path.exists(src_path):
        print(f"Error: Source file not found: {src_path}")
        continue
        
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    
    left = int(w * crop_pct)
    top = int(h * crop_pct)
    right = int(w * (1 - crop_pct))
    bottom = int(h * (1 - crop_pct))
    cropped = img.crop((left, top, right, bottom))
    
    for size in SIZES:
        resized = cropped.resize((size, size), Image.Resampling.LANCZOS)
        dest_path = os.path.join(THEME_DIR, f"{size}x{size}", category, filename)
        resized.save(dest_path, "PNG")
    print(f"Compiled: {filename}")

# 6. Generate relative symlinks for duplicate names
print("\n=== Generating Relative Symlinks for Duplicate Names ===")
symlink_count = 0
for category, mappings in COPY_MAPPINGS.items():
    for link_name, src_name in mappings.items():
        for size in SIZES:
            dest_dir = os.path.join(THEME_DIR, f"{size}x{size}", category)
            link_path = os.path.join(dest_dir, link_name)
            
            # Switch to directory to make symlinks relative
            original_cwd = os.getcwd()
            os.chdir(dest_dir)
            
            if os.path.exists(link_name) or os.path.islink(link_name):
                os.remove(link_name)
                
            os.symlink(src_name, link_name)
            symlink_count += 1
            os.chdir(original_cwd)
        print(f"Created symlink: {link_name} -> {src_name}")

print(f"\nCreated {symlink_count} relative symlinks across all size folders.")

# 7. Create index.theme
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

print("\n=== Rebuild and Symlink Complete ===")
