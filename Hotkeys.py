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
        scope = "user-modify-playback-state, user-read-playback-state"

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
        self.is_running = False

    def volume_increase(self):
        if self.sp.current_playback() != None:
            print("volume hoch")
            volume = self.sp.current_playback()["device"]["volume_percent"]  # type: ignore
            if volume < 100:
                volume += 10
            self.sp.volume(volume)

    def volume_decrease(self):
        if self.sp.current_playback() != None:
            print("volume runter")
            volume = self.sp.current_playback()["device"]["volume_percent"]  # type: ignore
            if volume > 0:
                volume -= 10
            self.sp.volume(volume)

    def play_pause(self):
        if self.sp.current_playback() != None:
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
        else:
            print("kein Gerät verbunden")


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
        if not "Spotify.exe" in (p.name() for p in psutil.process_iter()):
            print("Spotify wurde geöffnet")
            subprocess.call(
                r'start /b "" "C:\Users\fabia\AppData\Roaming\Spotify\Spotify.exe"',
                shell=True,
            )


if __name__ == "__main__":
    # sleep(10)
    # print("Hotkey wurde gestartet")
    # subprocess.call(r"taskkill /im FnaticOP.exe", shell=True)
    spotify = Spotify()
    hotkey = Hotkeys(spotify)
    hotkey.spotify_öffnen()
    keyboard.wait()
