# i3blocks-spotify
Very simple Python script to display artist name and track title on i3blocks.

Requires python-dbus library. Works on both Python 2 and Python3.

Disappears when Spotify is closed.

# Usage
```
# Spotify icon \uF1BC
[spotify]
label=
command=~/.config/i3blocks/scripts/spotify.py
color=#81b71a
interval=5
```

# Controls

Mouse clicks (left/right) to go forward/backward through tracks and to pause/play with middle-click. 
