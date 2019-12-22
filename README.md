To install clone this repository
Then in ~/.config/pianobar create two fifos with 
```
mkfifo ctl
mkfifo media
```
then in ~/.config/pianobar/config add
```
event_command = dir/to/this/repo/command
fifo = ~/.config/pianobar/ctl
```


then running pianobar-mediaplayer2 found in this repo should work.
If you are writing your own dbus commands this program will be reachable at org.mpris.MediaPlayer2.pianobar 

The ctl does not reliably work if you input text into the spawned terminal. In that case to quit you will have to manually quit using the spawned pianobar terminal.



