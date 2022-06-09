from infi.systray import SysTrayIcon
from time import sleep
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import keyboard

values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

icons = {0.0 : "icon/00.ico",
         0.1 : "icon/10.ico",
         0.2 : "icon/20.ico",
         0.3 : "icon/30.ico",
         0.4 : "icon/40.ico",
         0.5 : "icon/50.ico",
         0.6 : "icon/60.ico",
         0.7 : "icon/70.ico",
         0.8 : "icon/80.ico",
         0.9 : "icon/90.ico",
         1.0 : "icon/99.ico",
 }

def get_value():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            value = (volume.GetMasterVolume())
            return float(("{:.1f}".format(value)))

def update():
    print("update")
    sleep(.1)
    value = get_value()
    if value in values:
        systray.update(icon=icons[value])
        


if __name__ == "__main__":
    systray = SysTrayIcon("icon/00.ico", "spotify volume")
    systray.start()
    while True:
        sleep(1)
        update()

    # keyboard.add_hotkey("pagedown", update) 
    # keyboard.add_hotkey("pagedown", update)
    # keyboard.wait()
