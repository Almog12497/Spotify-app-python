import spotipy
import secrets
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='fbf69ccb8a4f40be9e0a3a618bad0e7f',
                                               client_secret='64a292f98d0740168005ef43f74a8411',
                                               redirect_uri="http://localhost/",
                                               scope="user-read-recently-played"))

offest=0
"""
results = sp.current_user_saved_tracks(50,offest,None)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx+offest, track['artists'][0]['name'], " – ", track['name'])"""

songs = sp.current_user_recently_played()

for idx , item in enumerate(songs['items']):
    track =item['track']
    print (idx+offest, track['artists'][0]['name'], " – ", track['name']) 
