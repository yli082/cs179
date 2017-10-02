import spotipy, json, pprint, sys
 
sp = spotipy.Spotify()
pp = pprint.PrettyPrinter(indent=4)

query = "weezer"

results = sp.search(q='artist:'+query, type='artist')
uri = results['artists']['items'][0]['uri']

name = results['artists']['items'][0]['name']
if name.lower() != query.lower():
	print "Error"
	sys.exit()

artist_dict = {}
artist_dict[name] = {}
artist_dict[name]['albums'] = []

artist_dict[name]['genres'] = results['artists']['items'][0]['genres']
artist_dict[name]['followers'] = results['artists']['items'][0]['followers']['total']
artist_dict[name]['popularity'] = results['artists']['items'][0]['popularity']


results = sp.artist_albums(uri, album_type='album')

#need to remove duplicates?
album_uris = []
for i in results['items']:
	album_uris.append(i['uri'])

results = sp.albums(album_uris)

track_uris = []
for i in results['albums']:
	artist_dict[name]['albums'].append({})
	artist_dict[name]['albums'][-1]['total_tracks'] = i['tracks']['total']
	artist_dict[name]['albums'][-1]['name'] = i['name']
 	artist_dict[name]['albums'][-1]['uri'] = i['uri']
	artist_dict[name]['albums'][-1]['popularity'] = i['popularity']
	artist_dict[name]['albums'][-1]['release_date'] = i['release_date']
	artist_dict[name]['albums'][-1]['tracks'] = []
	for j in i['tracks']['items']:
		artist_dict[name]['albums'][-1]['tracks'].append({})
		artist_dict[name]['albums'][-1]['tracks'][-1]['duration'] = j['duration_ms']
		artist_dict[name]['albums'][-1]['tracks'][-1]['name'] = j['name']
		artist_dict[name]['albums'][-1]['tracks'][-1]['uri'] = j['uri']

#print json.dumps(artist_dict, ensure_ascii=True)
pp.pprint(artist_dict)


