import dbus
import dbus.service
# import random

# god bless
# https://stackoverflow.com/questions/3740903/python-dbus-how-to-export-interface-property

# propPath="dbus.PROPERTIES_IFACE"
propPath = "org.freedesktop.DBus.Properties"


class mediaPlayer(dbus.service.Object):
    def __init__(self):
        self.bus = dbus.SessionBus()
        # ins=str(random.randrange(10000))
        name = dbus.service.BusName("org.mpris.MediaPlayer2.pianobar", bus=self.bus)
        super().__init__(name, "/org/mpris/MediaPlayer2")

        baseProperties = {
            "CanQuit": False,
            "CanRaise": False,
            "HasTrackList": False,
            "Identity": "Please Set",
            "SupportedUriSchemes": ["none"],
            "SupportedMimeTypes": ["none"],
        }
        playerProperties = {
            "PlaybackStatus": "Stopped",
            "Rate": 1.0,
            "Metadata": {"mpris:trackid":dbus.ObjectPath("/bogus/id",variant_level=1)},
            "Volume": 1.0,
            "Position": 1,
            "MinimumRate": 1.0,
            "MaximumRate": 1.0,
            "CanGoNext": False,
            "CanGoPrevious": False,
            "CanPlay": False,
            "CanPause": False,
            "CanSeek": False,
            "CanControl": False,
        }
        self.properties = {
            "org.mpris.MediaPlayer2": baseProperties,
            "org.mpris.MediaPlayer2.Player": playerProperties,
        }

        basePropertiesCanWrite = {
            "CanQuit": False,
            "CanRaise": False,
            "HasTrackList": False,
            "Identity": False,
            "SupportedUriSchemes": False,
            "SupportedMimeTypes": False,
        }
        playerPropertiesCanWrite = {
            "PlaybackStatus": False,
            "Rate": False,
            "Metadata": False,
            "Volume": False,
            "Position": False,
            "MinimumRate": False,
            "MaximumRate": False,
            "CanGoNext": False,
            "CanGoPrevious": False,
            "CanPlay": False,
            "CanPause": False,
            "CanSeek": False,
            "CanControl": False,
        }
        self.propertiesCanWrite = {
            "org.mpris.MediaPlayer2": basePropertiesCanWrite,
            "org.mpris.MediaPlayer2.Player": playerPropertiesCanWrite,
        }

        self.propertyValidator = {
            "org.mpris.MediaPlayer2": {},
            "org.mpris.MediaPlayer2.Player": {},
            "org.mpris.MediaPlayer2.TrackList": {},
            "org.mpris.MediaPlayer2.Playlists": {},
        }

    @dbus.service.method(propPath, in_signature="ss", out_signature="v")
    def Get(self, interfaceName, propertyName):
        return self.GetAll(interfaceName)[propertyName]

    @dbus.service.method(propPath, in_signature="s", out_signature="a{sv}")
    def GetAll(self, interfaceName):
        if interfaceName in self.properties.keys():
            return self.properties[interfaceName]
        else:
            raise dbus.exceptions.DBusException(
                "org.mpris.MediaPlayer2.UnknownInterface",
                "The Media player does not implement {0}".format(interaceName),
            )

    @dbus.service.method(propPath, in_signature="ssv")
    def Set(self, interfaceName, propertyName, newValue):
        if interfaceName in self.propertiesCanWrite.keys():
            if propertyName in self.propertiesCanWrite[interfaceName].keys():
                canWrite = self.propertiesCanWrite[interfaceName][propertyName]
            else:
                # should this be an error?
                pass
        else:
            raise dbus.exceptions.DBusException(
                "org.mpris.MediaPlayer2.UnknownInterface",
                "The Media Player Does not implement {0}".format(interfaceName),
            )
        if canWrite:
            valid = self.propertyValidator[interfaceName].setdefault(
                propertyName, lambda x: True
            )(newValue)
            if valid:
                self.properties[interfaceName][propertyName] = newValue
                self.PropertiesChanged(interfaceName, {propertyName: newValue}, [])

    @dbus.service.signal(propPath, signature="sa{sv}as")
    def PropertiesChanged(
        self, interfaceName, changedProperties, invalidatedProperties
    ):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2", out_signature="")
    def Raise(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2", out_signature="")
    def Quit(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", out_signature="")
    def Next(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", out_signature="")
    def Previous(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", out_signature="")
    def Pause(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", out_signature="")
    def PlayPause(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", out_signature="")
    def Stop(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", out_signature="")
    def Play(self):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", in_signature="x")
    def Seek(self, Offset):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", in_signature="ox")
    def SetPosition(self, TrackId, Position):
        pass

    @dbus.service.method("org.mpris.MediaPlayer2.Player", in_signature="s")
    def OpenUri(self, URI):
        pass

# vim: set tabstop=4 expandtab
