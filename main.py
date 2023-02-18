import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os 
import sys
from dotenv import load_dotenv

load_dotenv()

# GET OUR APPS ID AND SECRET FROM ENV FILE
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# AUTHENTICATES OUR APP AS A PSEUDO-SPOTIFY USER
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# ARTIST PROMPT
what_artist = input("What artist do you want to search for? ")

# IF NO ARGUMENT END PROGRAM
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = what_artist

# SEARCH FOR ARTISTS WITH q='artist:' AND MAKE SURE OUR RESULTS ARE LIMITED TO ARTISTS WITH type='artist'
results = sp.search(q='artist:' + name, type='artist')

# ITEMS = EVERY ARTIST FOUND FROM THE SEARCH + THEIR METADATA
items = results['artists']['items']

# IF NO RESULT DO NOTHING. IF AT LEAST 1 RESULT DO THE FOLLOWING
if len(items) > 0:
    # items[0] LIMITS OUR RESULTS TO THE TOP ARTIST AKA THE ARTIST WHO MATCHES OUR INPUT THE CLOSEST
    artist = items[0]
    # artist['uri'] IS ESSENTIALLY A UNIQUE CODE TIED TO EVERY ARTIST ON SPOTIFY
    # TO US IT'S IMPORTANT CAUSE ONCE WE HAVE IT WE CAN ACCESS THAT ARTIST A LOT FASTER BY NOT HAVING TO SERCH AGAIN
    artist_id = artist['uri']
    print("Name: " + artist['name'] + "\n" + "ID: " + artist_id)