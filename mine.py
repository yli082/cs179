import spotipy

sp = spotipy.Spotify()

results = sp.search(q='artist:weezer', type='artist')

uri = results['artists']['items'][0]['uri']
#print results['artists']['items'][0]['genres']
print results['artists']['items'][0]

results = sp.artist_albums(uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

f = open("test", 'w')

for album in albums:
    uri = album['uri']
    f.write(uri)
    results = sp.album_tracks(uri)
    for i in results['items']:
	    f.write(i['name'].encode('utf-8'))
    f.write("---------------")
f.close()

