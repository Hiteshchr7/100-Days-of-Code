import os
import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.environ.get("sp_client_id")
client_secret = os.environ.get("sp_client_secret")
scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=os.environ.get("redirect_uri"),
        scope=scope,
        cache_path="WEB DEVELOPMENT/Day 46/token.txt"  #specify the path where you want your token.txt
    )
)

user_id = sp.current_user()["id"]
date = input("What year would you like to travel to? Type the data in this format YYYY-MM-DD: ")
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
url = f"https://www.billboard.com/charts/hot-100/{date}"

year = date.split("-")[0]

response = requests.get(url, headers=header)
if response.status_code != 200:
    print(f"Failed to fetch Billboard page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.select("li ul li h3")
if not songs:
    print("Could not find any songs on Billboard page. The site structure may have changed.")
    exit()

top_100_billboards = [song.getText(strip=True) for song in songs]

song_uris = []
for song in top_100_billboards:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"{date} Top_100_Billboards"

playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False
)
print(f"Created new playlist: {playlist_name}")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"✅ Playlist ready: {playlist['external_urls']['spotify']}")
