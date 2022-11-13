#bin/bash
sudo pacman -Sy git python --noconfirm && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si