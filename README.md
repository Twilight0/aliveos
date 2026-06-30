# AliveOS (Cinnamon Spin)

AliveOS is a custom, lightweight, and modern Linux distribution based on **Garuda/Arch Linux**, featuring the **Cinnamon Desktop**, **XLibre display server**, and automated builds via **GitHub Actions**.

## Key Features
*   **Base:** Arch Linux with system performance tweaks.
*   **Repositories:** Integrates `core`, `extra`, `multilib`, `garuda`, `chaotic-aur`, and `xlibre` repositories.
*   **Display Server:** XLibre (the modern X11 replacement community fork).
*   **Desktop:** Cinnamon (minimal setup with no preloaded bloatware).
*   **Autologin:** Automatically logs into the live environment as `liveuser`.
*   **Installer:** Calamares GUI installer.

---

## Repository Structure
```text
aliveos/
├── .github/
│   └── workflows/
│       └── build-iso.yml        # GitHub Actions CI/CD ISO pipeline
├── profile/                     # Archiso configuration profile
│   ├── pacman.conf             # Profile pacman.conf with custom repositories
│   ├── packages.x86_64         # Minimal package list (XLibre + Cinnamon)
│   ├── profiledef.sh           # Archiso metadata and permission specifications
│   └── airootfs/               # Overlay filesystem injected into the Live image
│       ├── etc/
│       │   ├── hostname        # Hostname configuration ('aliveos')
│       │   ├── os-release      # AliveOS OS information and branding
│       │   ├── lsb-release     # Linux Standard Base configuration
│       │   └── systemd/        # Systemd live boot services
│       └── usr/
│           └── share/
│               └── backgrounds/
│                   └── aliveos/ # Branding assets (default.png)
└── scripts/
    └── build.sh                # Local helper build script (requires root/sudo)
```

---

## Building Locally

To build the ISO locally, you need an Arch Linux or Arch-based host system with `archiso` installed:

1.  **Install dependencies:**
    ```bash
    sudo pacman -S archiso git
    ```

2.  **Run the build script:**
    ```bash
    sudo ./scripts/build.sh
    ```

The completed ISO file will be generated in `out/`.

---

## Building via CI/CD (GitHub Actions)

AliveOS is fully automated. When you push this project to GitHub:

1.  GitHub Actions will start a job in a privileged Arch Linux docker container.
2.  It will assemble the packages, copy the filesystem overlay and wallpaper, and build a bootable ISO.
3.  **On Push/Main:** The ISO is uploaded as a run artifact (available for download in the Actions tab).
4.  **On Release Tag (e.g. `v1.0.0`):** The workflow will automatically create a new GitHub Release and attach the compiled `.iso` file directly as a release asset.
