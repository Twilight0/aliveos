#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="aliveos"
iso_label="ALIVEOS_$(date +%Y%m)"
iso_publisher="AliveOS Project"
iso_application="AliveOS Cinnamon Live/Install Media"
iso_version="$(date +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito' 'uefi-x64.systemd-boot.esp' 'uefi-x64.systemd-boot.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"

file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/gshadow"]="0:0:400"
  ["/etc/sudoers.d"]="0:0:750"
  ["/root"]="0:0:700"
  ["/usr/local/bin/aliveos-live-init"]="0:0:755"
)
