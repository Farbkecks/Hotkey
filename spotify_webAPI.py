import os
import spotipy
import spotipy.util as util
import Token
from json.decoder import JSONDecodeError


# Set data client, redirect URL and username
username = "farbkecks26"
client_id = Token.CLIENT_ID
client_secret = Token.CLIENT_SECRET
redirect_uri = Token.SPOTIPY_REDIRECT_URI
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
sp = spotipy.Spotify(auth=token)
current = sp.next_track()


# if __name__ == "__main__":
#     # token_test()
#     print(get_token())
