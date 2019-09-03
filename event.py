#! /usr/bin/python

# Copyright (C) 2012 Maxwell J. Koo <mjkoo90@gmail.com>
#
# Based on code originally by John Reese, LeetCode.net
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import contextlib
import dbus
import os
import sys


def handle_event(type, **kwargs):
    """
    Read event parameters from stdin and handle events appropriately.
    """

    # Error from pianobar, disregard
    if kwargs.get("pRet") != "1":
        return

    # Handle specific events
    if type == "songstart":
        title = kwargs.get("title")

        artist_album = "by %s on %s" % (kwargs.get("artist"), kwargs.get("album"))
        config_dir = os.path.abspath(os.path.dirname(sys.argv[0]))


        obj_path = "/org/mpris/MediaPlayer2"
        iface_name = "org.freedesktop.DBUS.Properties"
        bus_name = "org.mpris.MediaPlayer2.pianobar"
        bus = dbus.SessionBus()
        obj = bus.get_object(bus_name, obj_path)
        iface = dbus.Interface(obj, iface_name)

        iface.Notify("", 0, 0, title, artist_album, [], [], 5000)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # Read event type from command arguments
    if len(sys.argv) < 2:
        print "error reading event type from command arguments"

    type = sys.argv[1]

    # Read parameters from input
    params = {}
    for s in sys.stdin.readlines():
        param, value = s.split("=", 1)
        params[param.strip()] = value.strip()

    # Call the event handler
    handle_event(type, **params)
    print "testing this even works"+str(argv)
    return 0

if __name__ == "__main__":
    sys.exit(main())
