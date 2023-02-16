import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os 

os.environ['SPOTIPY_CLIENT_ID'] = '4d795cbc2b55405bb35855e195ad1b8b'
os.environ['SPOTIPY_CLIENT_SECRET'] = '25911e66cd7e488aa0b51cb7937923c8'

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

print(sp.search(q="Pink Floyd", type="artist", limit=1))