import requests
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def extract_data(artist_id):
    # Use the Spotify API to get information about the artist's albums
    headers = {
        "Authorization": f"Bearer {get_access_token()}"
    }
    response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/albums", headers=headers)
    response.raise_for_status()
    albums = response.json()["items"]
    
    # Create a list of song names and album names
    songs = []
    for album in albums:
        album_name = album["name"]
        tracks_response = requests.get(album["href"], headers=headers)
        tracks_response.raise_for_status()
        tracks = tracks_response.json()["tracks"]["items"]
        for track in tracks:
            song_name = track["name"]
            songs.append((song_name, album_name))
    
    return songs

def get_access_token():
    # Use the Spotify API to get an access token
    response = requests.post("https://accounts.spotify.com/api/token", data={
        "grant_type": "client_credentials"
    }, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
    response.raise_for_status()
    return response.json()["access_token"]
