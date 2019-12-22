for terminal in "$TERMINAL" gnome-terminal xfce4-terminal xterm ; do
	if command -v "$terminal" > /dev/null 2>&1; then

		exec $terminal -e pianobar

	fi
done
