import subprocess

# from infi import systray
import psutil
from time import sleep
import keyboard
from infi.systray import SysTrayIcon


class Spotify:
    def __init__(self):
        self.value = -1

    def get_value(self):
        from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "Spotify.exe":
                value = volume.GetMasterVolume()
                # print("orginal value: " + str(value))
                self.value = int(float(("{:.1f}".format(value))) * 10)
                break
        else:
            # print("Spotify hat noch keine Audio abgespielt")
            self.value = -1


class Hotkeys:
    def __init__(self, spotify, anzeige):
        self.spotify = spotify
        self.anzeige = anzeige

        keyboard.add_hotkey("strg+ü", self.spotify_öffnen)
        keyboard.add_hotkey("strg+ä", self.spotify_schliessen)
        keyboard.add_hotkey("strg+i", self.show_vaule)
        keyboard.add_hotkey("F18", self.anzeige.update)
        keyboard.add_hotkey("F19", self.anzeige.update)

    def show_vaule(self):
        self.spotify.get_value()
        print(self.spotify.value)

    def spotify_schliessen(self):
        print("Spotify wurde geschlossen")
        subprocess.call(r"taskkill /im Spotify.exe /t /f", shell=True)

    def spotify_öffnen(self):
        if not "Toastify.exe" in (p.name() for p in psutil.process_iter()):
            print("Spotify wurde geöffnet")
            subprocess.call(
                r'start /b "" "C:\Program Files\Toastify\Toastify.exe"', shell=True
            )
        self.anzeige.update()


class Systray:
    def __init__(self, spotify):
        self.spotify = spotify
        # self.values = [0,1,2,3,4,5,6,7,8,9,10]
        self.icons = {
            0: "icon/00.ico",
            1: "icon/10.ico",
            2: "icon/20.ico",
            3: "icon/30.ico",
            4: "icon/40.ico",
            5: "icon/50.ico",
            6: "icon/60.ico",
            7: "icon/70.ico",
            8: "icon/80.ico",
            9: "icon/90.ico",
            10: "icon/99.ico",
        }
        self.systray = SysTrayIcon("icon/f.ico", "spotify volume")
        self.systray.start()
        self.update()

    def update(self):
        sleep(0.1)
        self.spotify.get_value()
        # print("Value: "+ str(self.spotify.value))
        if self.spotify.value == -1:
            self.systray.update(icon="icon/f.ico")
            print("Spotify hat noch keine Musik abgespielt")
        else:
            self.systray.update(icon=self.icons[self.spotify.value])


if __name__ == "__main__":
    sleep(10)
    print("Hotkey wurde gestartet")
    subprocess.call(r"taskkill /im FnaticOP.exe", shell=True)
    spotify = Spotify()
    anzeige = Systray(spotify)
    hotkey = Hotkeys(spotify, anzeige)
    hotkey.spotify_öffnen()
    keyboard.wait()
