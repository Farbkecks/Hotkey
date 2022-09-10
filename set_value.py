def set_value(value):
    from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

    found = False
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "Spotify.exe":
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(value, None)
            break
    else:
        print("Spotify hat noch keine Audio abgespielt")


set_value(0.3)
