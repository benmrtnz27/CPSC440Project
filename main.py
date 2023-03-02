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

def get_artist(name):
    '''Function to get artists. This will be used as arguments for other functions.'''
    results = sp.search(q="artist:" + name, type="artist")
    items = results['artists']['items']
    if len(items) > 0:
        # print(items)  If you want to see the metadata to an artist
        return items[0] 
    else:
        return None
    
def show_track_recommendations_for_artist(artist):
    '''Returns songs based on an artist.'''
    print(artist['name'] + ' Recommened Tracks:')
    results = sp.recommendations(seed_artists=[artist['id']])
    # print(results)
    for track in results['tracks']:
        if track['artists'][0]['name'] != artist['name']:
            print(track['artists'][0]['name'] + ": " + track['name'])

def show_artists_recommendations_for_artist(artist):
    '''Returns artists based on an artist.'''
    print(artist['name'] + " Recommended Artists:")
    results = sp.recommendations(seed_artists=[artist['id']])
    artist_list = set()
    for artist_rec in results['tracks']:
        artist_list.add(artist_rec['artists'][0]['name']) 
    artist_list.discard(artist['name'])
    for artist_name in artist_list:
        print(artist_name)


artist = get_artist(name)
answer = input("What do you want to be recommened? \n1. Songs \n2. Artists \n")
if answer == "1":
    show_track_recommendations_for_artist(artist)
    playlist_create_prompt = input("Would you like to create a playlist out of the recommended tracks? (1) Or just play the songs? (2)")
    # TODO
elif answer == "2": 
    show_artists_recommendations_for_artist(artist)
    artist_recommendations_get_songs_prompt = input("Would you like to create a playlist out of the recommended artists? (1) Or just play their top songs? (2)")
    # TODO