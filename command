#!/bin/sh

# don't block pianobar if pianobar-mediaplayer2 is not running
pkill -0 -f pianobar-mediaplayer2 || exit 1

echo "$@" > ~/.config/pianobar/media
cat $input > ~/.config/pianobar/media
