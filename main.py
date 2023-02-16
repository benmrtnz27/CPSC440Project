import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os 
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

print(sp.search(q="Pink Floyd", type="artist", limit=1))