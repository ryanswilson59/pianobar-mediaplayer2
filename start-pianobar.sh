for terminal in "$TERMINAL" gnome-terminal xfce4-terminal xterm ; do
	if command -v "$terminal" > /dev/null 2>&1; then
		if [ $terminal == gnome-terminal ]
		then
			exec gnome-terminal -- pianobar
		else
			exec $terminal -e pianobar
		fi
	fi
done

gnome-terminal -- pianobar
