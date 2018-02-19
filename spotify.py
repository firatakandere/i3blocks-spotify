#!/usr/bin/python

import dbus

# Uncomment the following lines if you have playerctl installed to allow
# Left/right clicking to play next/previous songs

#import os
#if os.environ.get('BLOCK_BUTTON'):
#    os.system({
#        '1': "playerctl previous",
#        '2': "playerctl play-pause",
#        '3': "playerctl next",
#    }[os.environ['BLOCK_BUTTON']])

try:
	bus = dbus.SessionBus()
	spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
	spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
	props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
	print(str(props['xesam:artist'][0]) + " - " + str(props['xesam:title']))
	exit
except dbus.exceptions.DBusException:
	exit



