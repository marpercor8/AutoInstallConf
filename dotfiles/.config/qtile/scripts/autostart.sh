#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
imwheel &
lxsession &
flameshot &

run nm-applet
run nitrogen --restore
run picom -b
run lxpolkit
run nm-applet
run volumeicon
run urxvtd -q -o -f
run emacs --daemon

feh --randomize --bg-fill /usr/share/backgrounds/archlinux/*
