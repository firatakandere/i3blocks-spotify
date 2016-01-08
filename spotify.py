#!/usr/bin/python

import dbus
try:
	bus = dbus.SessionBus()
	spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
	spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
	props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
	print(str(props['xesam:artist'][0]) + " - " + str(props['xesam:title']))
	exit
except dbus.exceptions.DBusException:
	exit



