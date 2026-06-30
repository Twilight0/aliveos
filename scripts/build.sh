#!/usr/bin/env bash

# Exit on error
set -e

# Make sure the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Error: This script must be run as root (or via sudo) to generate chroots."
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== AliveOS ISO Build Tool ==="
echo "Project Directory: $PROJECT_DIR"
cd "$PROJECT_DIR"

# 1. Setup local symlinks
echo "Setting up systemd symlinks..."
mkdir -p profile/airootfs/etc/systemd/system/multi-user.target.wants
mkdir -p profile/airootfs/etc/systemd/system/display-manager.service.wants

ln -sf /usr/lib/systemd/system/NetworkManager.service profile/airootfs/etc/systemd/system/multi-user.target.wants/NetworkManager.service
ln -sf /usr/lib/systemd/system/aliveos-live-init.service profile/airootfs/etc/systemd/system/multi-user.target.wants/aliveos-live-init.service
ln -sf /usr/lib/systemd/system/lightdm.service profile/airootfs/etc/systemd/system/display-manager.service

# 2. Cleanup previous runs
echo "Cleaning up work and out directories..."
rm -rf work out
mkdir -p work out

# 3. Build the ISO
echo "Running mkarchiso..."
mkarchiso -v -w work -o out profile

echo "=== Build Complete! ==="
echo "ISO generated in: $PROJECT_DIR/out/"
ls -lh out/
