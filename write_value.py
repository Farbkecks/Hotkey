from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def get_value():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            value = (volume.GetMasterVolume())
            return float(("{:.1f}".format(value)))

value = str(get_value()*10)

file = open("value.txt", "w")
file.write(value)
file.close()