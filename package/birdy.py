import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def birdy_albums():
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']

    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    albums_names = []

    for album in albums:
        albums_names.append(album['name'])

    return albums_names
