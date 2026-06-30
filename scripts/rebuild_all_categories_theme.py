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

# 1. Base designs mappings (where each target file in a category gets compiled from its JPEG source)
CORE_COMPILATIONS = {
    "places": {
        "user-home.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_home_borderless_1782684216790.jpg",
            "crop": 0.05
        },
        "user-trash.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_trash_borderless_1782684340875.jpg",
            "crop": 0.06
        }
    },
    "apps": {
        "preferences-system.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_settings_borderless_1782684245688.jpg",
            "crop": 0.02
        },
        "utilities-terminal.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_terminal_borderless_1782684277441.jpg",
            "crop": 0.02
        },
        "internet-web-browser.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_browser_borderless_1782684308750.jpg",
            "crop": 0.12
        },
        "accessories-text-editor.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_text_editor_1782684601449.jpg",
            "crop": 0.05
        },
        "multimedia-player.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_media_1782684764797.jpg",
            "crop": 0.15
        },
        "utilities-system-monitor.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_monitor_1782684641139.jpg",
            "crop": 0.02
        },
        "system-software-install.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_store_clean_1782684721862.jpg",
            "crop": 0.15
        },
        "network-wireless.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_network_1782685087608.jpg",
            "crop": 0.15
        },
        "audio-volume-high.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_audio_1782685127179.jpg",
            "crop": 0.20
        },
        "x-office-document.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_office_1782685172145.jpg",
            "crop": 0.05
        }
    },
    "actions": {
        "go-home.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_home_borderless_1782684216790.jpg",
            "crop": 0.05
        },
        "edit-delete.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_trash_borderless_1782684340875.jpg",
            "crop": 0.06
        },
        "system-shutdown.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_settings_borderless_1782684245688.jpg",
            "crop": 0.02
        },
        "edit-find.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_browser_borderless_1782684308750.jpg",
            "crop": 0.12
        },
        "document-save.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_office_1782685172145.jpg",
            "crop": 0.05
        }
    },
    "devices": {
        "computer.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_monitor_1782684641139.jpg",
            "crop": 0.02
        },
        "audio-card.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_audio_1782685127179.jpg",
            "crop": 0.20
        },
        "network-wired.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_network_1782685087608.jpg",
            "crop": 0.15
        }
    },
    "mimetypes": {
        "text-x-generic.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_office_1782685172145.jpg",
            "crop": 0.05
        },
        "audio-x-generic.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_media_1782684764797.jpg",
            "crop": 0.15
        },
        "video-x-generic.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_media_1782684764797.jpg",
            "crop": 0.15
        },
        "image-x-generic.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_browser_borderless_1782684308750.jpg",
            "crop": 0.12
        }
    },
    "preferences": {
        "preferences-desktop.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_settings_borderless_1782684245688.jpg",
            "crop": 0.02
        }
    },
    "status": {
        "network-wireless-connected.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_network_1782685087608.jpg",
            "crop": 0.15
        },
        "audio-volume-high.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_audio_1782685127179.jpg",
            "crop": 0.20
        },
        "dialog-error.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_trash_borderless_1782684340875.jpg",
            "crop": 0.06
        },
        "dialog-information.png": {
            "src": "/home/twilight/.gemini/antigravity-cli/brain/5211d070-d537-448c-bd93-06de05750447/aliveos_home_borderless_1782684216790.jpg",
            "crop": 0.05
        }
    }
}

# 2. Local Symlink Mapping configurations
# Key: Category -> { Symlink Name : Local Source Name }
SYMLINK_MAPPINGS = {
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
    },
    "actions": {
        "go-home-symbolic.png": "go-home.png",
        "edit-delete-symbolic.png": "edit-delete.png",
        "system-log-out.png": "system-shutdown.png",
        "system-lock-screen.png": "system-shutdown.png",
        "system-reboot.png": "system-shutdown.png",
        "edit-find-symbolic.png": "edit-find.png",
        "search.png": "edit-find.png",
        "document-new.png": "document-save.png",
        "document-save-as.png": "document-save.png"
    },
    "devices": {
        "display.png": "computer.png",
        "input-keyboard.png": "computer.png",
        "input-mouse.png": "computer.png",
        "audio-input-microphone.png": "audio-card.png",
        "network-wireless.png": "network-wired.png",
        "network-server.png": "network-wired.png"
    },
    "mimetypes": {
        "application-pdf.png": "text-x-generic.png",
        "application-x-executable.png": "text-x-generic.png",
        "sound.png": "audio-x-generic.png",
        "movie.png": "video-x-generic.png",
        "image-png.png": "image-x-generic.png",
        "image-jpeg.png": "image-x-generic.png"
    },
    "preferences": {
        "preferences-system.png": "preferences-desktop.png",
        "preferences-desktop-wallpaper.png": "preferences-desktop.png",
        "preferences-desktop-keyboard.png": "preferences-desktop.png"
    },
    "status": {
        "network-wired-connected.png": "network-wireless-connected.png",
        "network-transmit-receive.png": "network-wireless-connected.png",
        "audio-volume-low.png": "audio-volume-high.png",
        "audio-volume-medium.png": "audio-volume-high.png",
        "audio-volume-muted.png": "audio-volume-high.png",
        "dialog-warning.png": "dialog-error.png"
    }
}

CATEGORIES = ["apps", "places", "actions", "devices", "mimetypes", "preferences", "status"]
SIZES = [16, 22, 32, 48, 64, 128, 256]

# 3. Re-initialize Theme folder completely
print("=== Re-initializing AliveOS Rich Multi-Category Theme ===")
if os.path.exists(THEME_DIR):
    shutil.rmtree(THEME_DIR)
    print(f"Deleted old icon theme folder: {THEME_DIR}")

# Create directories
for size in SIZES:
    for cat in CATEGORIES:
        os.makedirs(os.path.join(THEME_DIR, f"{size}x{size}", cat), exist_ok=True)
print("Created layout paths for all 7 sizes across 7 categories.")

# 4. Perform Core compilations
print("\n=== Compiling Core Category PNG Icons ===")
for category, icons in CORE_COMPILATIONS.items():
    for filename, info in icons.items():
        src_path = info["src"]
        crop_pct = info["crop"]
        
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
        print(f"Compiled: {category}/{filename}")

# 5. Perform relative symlink mapping
print("\n=== Generating Symlinks for all categories ===")
symlink_count = 0
for category, mappings in SYMLINK_MAPPINGS.items():
    for link_name, src_name in mappings.items():
        for size in SIZES:
            dest_dir = os.path.join(THEME_DIR, f"{size}x{size}", category)
            
            # Switch directory to make symlink relative
            original_cwd = os.getcwd()
            os.chdir(dest_dir)
            
            # Remove previous link/file if existing
            if os.path.exists(link_name) or os.path.islink(link_name):
                os.remove(link_name)
                
            os.symlink(src_name, link_name)
            symlink_count += 1
            os.chdir(original_cwd)
        print(f"Created: {category}/{link_name} -> {src_name}")

print(f"\nGenerated {symlink_count} relative symlinks.")

# 6. Generate rich index.theme definition listing all categories
dir_definitions = []
dir_sections = []

for size in SIZES:
    for cat in CATEGORIES:
        section_name = f"{size}x{size}/{cat}"
        dir_definitions.append(section_name)
        
        context_name = "Applications"
        if cat == "places":
            context_name = "Places"
        elif cat == "actions":
            context_name = "Actions"
        elif cat == "devices":
            context_name = "Devices"
        elif cat == "mimetypes":
            context_name = "MimeTypes"
        elif cat == "preferences":
            context_name = "Preferences"
        elif cat == "status":
            context_name = "Status"
            
        dir_sections.append(f"""
[{section_name}]
Size={size}
Context={context_name}
Type=Fixed""")

directories_line = ",".join(dir_definitions)

index_theme_content = f"""[Icon Theme]
Name=AliveOS
Comment=Complete custom neon dark square icon theme for AliveOS
Inherits=Papirus-Dark,Adwaita,hicolor
Directories={directories_line}
""" + "".join(dir_sections)

index_path = os.path.join(THEME_DIR, "index.theme")
with open(index_path, "w") as f:
    f.write(index_theme_content)
print(f"\nCreated index.theme configuration: {index_path}")

print("\n=== Rich Theme Rebuild Complete ===")
