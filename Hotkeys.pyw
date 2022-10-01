import subprocess
import os
import spotipy
import spotipy.util as util
import Token
from json.decoder import JSONDecodeError

# from infi import systray
import psutil
from time import sleep
import keyboard

# from infi.systray import SysTrayIcon


class Spotify:
    def __init__(self):
        # Set data client, redirect URL and username
        username = "farbkecks26"
        client_id = Token.CLIENT_ID
        client_secret = Token.CLIENT_SECRET
        redirect_uri = "http://localhost"
        scope = "user-modify-playback-state"

        # Erase cache and prompt for user permission
        try:
            token = util.prompt_for_user_token(
                username, scope, client_id, client_secret, redirect_uri
            )
        except (AttributeError, JSONDecodeError):
            os.remove(f".cache-{username}")
            token = util.prompt_for_user_token(
                username, scope, client_id, client_secret, redirect_uri
            )

        # Configure Spotify
        self.sp = spotipy.Spotify(auth=token)
        self.volume = 30
        self.is_running = False

    def volume_increase(self):
        print("volume hoch")
        if self.volume < 100:
            self.volume += 10
        self.sp.volume(self.volume)

    def volume_decrease(self):
        print("volume 10 runter")
        if self.volume > 0:
            self.volume -= 10
        self.sp.volume(self.volume)

    def play_pause(self):
        print("play / pause")
        if self.is_running:
            try:
                self.sp.pause_playback()
                self.is_running = False
            except:
                self.sp.start_playback()

        else:
            try:
                self.sp.start_playback()
                self.is_running = True
            except:
                self.sp.pause_playback()


class Hotkeys:
    def __init__(self, spotify):
        self.spotify = spotify
        keyboard.add_hotkey("strg+ü", self.spotify_öffnen)
        keyboard.add_hotkey("strg+ä", self.spotify_schliessen)
        keyboard.add_hotkey("F23", self.spotify.volume_increase)
        keyboard.add_hotkey("F24", self.spotify.volume_decrease)
        keyboard.add_hotkey("F22", self.spotify.play_pause)

    def spotify_schliessen(self):
        print("Spotify wurde geschlossen")
        subprocess.call(r"taskkill /im Spotify.exe /t /f", shell=True)

    def spotify_öffnen(self):
        pass
        # if not "Toastify.exe" in (p.name() for p in psutil.process_iter()):
        #     print("Spotify wurde geöffnet")
        #     subprocess.call(
        #         r'start /b "" "C:\Program Files\Toastify\Toastify.exe"', shell=True
        #     )


if __name__ == "__main__":
    sleep(10)
    print("Hotkey wurde gestartet")
    subprocess.call(r"taskkill /im FnaticOP.exe", shell=True)
    spotify = Spotify()
    hotkey = Hotkeys(spotify)
    # hotkey.spotify_öffnen()
    keyboard.wait()
