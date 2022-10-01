import requests
from Token import CLIENT_ID, CLIENT_SECRET


import base64, requests, sys


# Encode the client ID and client secret
authorization = base64.b64encode(
    bytes(CLIENT_ID + ":" + CLIENT_SECRET, "ISO-8859-1")
).decode("ascii")


headers = {
    "Authorization": f"Basic {authorization}",
    "Content-Type": "application/x-www-form-urlencoded",
}
body = {"grant_type": "client_credentials"}

response = requests.post(
    "https://accounts.spotify.com/api/token", data=body, headers=headers
)

print(response.json()["access_token"])
