#!/usr/bin/env python3
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Installing python-pillow...")
    os.system("sudo pacman -S --noconfirm python-pillow")
    from PIL import Image

# 1. Paths of the 3 new core icons to crop and save
NEW_ICONS = {
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

PLACES_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/places"
APPS_DIR = "/home/twilight/Projects/aliveos/profile/airootfs/usr/share/icons/aliveos/apps"

os.makedirs(PLACES_DIR, exist_ok=True)
os.makedirs(APPS_DIR, exist_ok=True)

# 2. Process and crop new core icons
print("=== Cropping new core icons ===")
for filename, info in NEW_ICONS.items():
    filepath = info["src"]
    crop_pct = info["crop"]
    
    if not os.path.exists(filepath):
        print(f"Error: Source file does not exist: {filepath}")
        continue
        
    print(f"Cropping: {filename} (crop: {crop_pct})")
    img = Image.open(filepath)
    w, h = img.size
    
    left = int(w * crop_pct)
    top = int(h * crop_pct)
    right = int(w * (1 - crop_pct))
    bottom = int(h * (1 - crop_pct))
    
    cropped_img = img.crop((left, top, right, bottom))
    final_img = cropped_img.resize((256, 256), Image.Resampling.LANCZOS)
    
    dest_path = os.path.join(APPS_DIR if info["type"] == "apps" else PLACES_DIR, filename)
    final_img.save(dest_path, "PNG")
    print(f"Saved: {dest_path}")


# 3. Symlinking mapping dictionary
# Map: Target Name -> Source Name
SYMLINKS = {
    # Places Symlinks (Source is in places/)
    "places": {
        # Home folder maps
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
        # Trash states maps
        "user-trash-empty.png": "user-trash.png",
        "user-trash-full.png": "user-trash.png",
        "user-trash-empty-state.png": "user-trash.png",
        "user-trash-full-state.png": "user-trash.png"
    },
    # Apps Symlinks (Source is in apps/)
    "apps": {
        # System Settings
        "cinnamon-control-center.png": "preferences-system.png",
        "gnome-control-center.png": "preferences-system.png",
        "settings.png": "preferences-system.png",
        "preferences-desktop.png": "preferences-system.png",
        "preferences-system-details.png": "preferences-system.png",
        "system-settings.png": "preferences-system.png",
        "control-panel.png": "preferences-system.png",
        # Terminals
        "terminal.png": "utilities-terminal.png",
        "gnome-terminal.png": "utilities-terminal.png",
        "kitty.png": "utilities-terminal.png",
        "alacritty.png": "utilities-terminal.png",
        "xterm.png": "utilities-terminal.png",
        "konsole.png": "utilities-terminal.png",
        "utilities-terminal-alt.png": "utilities-terminal.png",
        # Web Browsers
        "web-browser.png": "internet-web-browser.png",
        "firefox.png": "internet-web-browser.png",
        "google-chrome.png": "internet-web-browser.png",
        "chromium.png": "internet-web-browser.png",
        "opera.png": "internet-web-browser.png",
        "brave-browser.png": "internet-web-browser.png",
        "vivaldi.png": "internet-web-browser.png",
        "epiphany.png": "internet-web-browser.png",
        "midori.png": "internet-web-browser.png",
        # Text Editors
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
        # Media Players
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
        # System Monitors
        "system-monitor.png": "utilities-system-monitor.png",
        "gnome-system-monitor.png": "utilities-system-monitor.png",
        "htop.png": "utilities-system-monitor.png",
        "btop.png": "utilities-system-monitor.png",
        "top.png": "utilities-system-monitor.png",
        # Software Installers
        "software-center.png": "system-software-install.png",
        "pamac-manager.png": "system-software-install.png",
        "discover.png": "system-software-install.png",
        "gourmet.png": "system-software-install.png",
        "synaptic.png": "system-software-install.png",
        "package-manager.png": "system-software-install.png",
        # Networks
        "network.png": "network-wireless.png",
        "network-wired.png": "network-wireless.png",
        "network-wireless-connected.png": "network-wireless.png",
        "network-workgroup.png": "network-wireless.png",
        "network-server.png": "network-wireless.png",
        # Audios
        "audio-volume-medium.png": "audio-volume-high.png",
        "audio-volume-low.png": "audio-volume-high.png",
        "audio-volume-muted.png": "audio-volume-high.png",
        "audio-card.png": "audio-volume-high.png",
        "volume.png": "audio-volume-high.png",
        "sound.png": "audio-volume-high.png",
        # Office
        "office.png": "x-office-document.png",
        "libreoffice-writer.png": "x-office-document.png",
        "libreoffice.png": "x-office-document.png",
        "document.png": "x-office-document.png",
        "wps-office-wps.png": "x-office-document.png"
    }
}

# 4. Generate Symlinks
print("\n=== Generating Symlinks ===")
for category, mappings in SYMLINKS.items():
    dest_dir = PLACES_DIR if category == "places" else APPS_DIR
    
    # Change cwd to make symlinks relative (best practice for portability)
    original_cwd = os.getcwd()
    os.chdir(dest_dir)
    
    for link_name, src_name in mappings.items():
        if not os.path.exists(src_name):
            print(f"Warning: Source file for symlink does not exist: {src_name}")
            continue
            
        # Remove existing symlink or file if present
        if os.path.exists(link_name) or os.path.islink(link_name):
            os.remove(link_name)
            
        os.symlink(src_name, link_name)
        print(f"Created symlink: {link_name} -> {src_name}")
        
    os.chdir(original_cwd)

print("\nAll symlinks generated successfully.")
