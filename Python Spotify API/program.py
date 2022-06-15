import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = '1y1b3eg69c00aackiy3bokmz5'

token = SpotifyOAuth(scope=scope, username=username)
spotifyObj = spotipy.Spotify(auth_manager= token)

# create playlist
playlist_name = input("Enter playlist name: ")
search_name = input("Enter song name: ")
list_of_songs = []
 
spotifyObj.user_playlist_create(user=username,name=playlist_name,public=True,description="Making this as a test of the api")

while search_name != 'quit':
    result = spotifyObj.search(q=search_name)
    #print(json.dumps(result,sort_keys=4,indent=4))
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    search_name = input("Enter song name: ")

prePlaylist = spotifyObj.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

# Add songs to playlist
spotifyObj.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)