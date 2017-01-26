import wikipedia, spotipy, json, pprint, sys

sp = spotipy.Spotify()
pp = pprint.PrettyPrinter(indent=4)
w = wikipedia.WikipediaPage(title="List of musicians")

for i in w.links:
        try:
		p = wikipedia.WikipediaPage(title=i)
        
		for j in p.links:
			print j.encode('utf-8')
			out = {}
			out[j.encode('utf-8')] = ''
			try:
				results = sp.search(q='artist:'+j.encode('utf-8'), type='artist')
				uri = results['artists']['items'][0]['uri']
				name = results['artists']['items'][0]['name']
				
				a = wikipedia.WikipediaPage(title=j)
				
				summary = a.summary
				content = a.content
				ref = a.references
				out[j.encode('utf-8')] = {}
				out[j.encode('utf-8')]['summary'] = summary
				out[j.encode('utf-8')]['content'] = content
				out[j.encode('utf-8')]['references'] = ref
				out[j.encode('utf-8')]['albums'] = []
				out[j.encode('utf-8')]['genres'] = results['artists']['items'][0]['genres']
				out[j.encode('utf-8')]['followers'] = results['artists']['items'][0]['followers']['total']
				out[j.encode('utf-8')]['popularity'] = results['artists']['items'][0]['popularity']


				results = sp.artist_albums(uri, album_type='album')

				#need to remove duplicates?
				album_uris = []
				for m in results['items']:
					album_uris.append(m['uri'])

				results = sp.albums(album_uris)
				
				track_uris = []
				for g in results['albums']:
					out[j.encode('utf-8')]['albums'].append({})
					out[j.encode('utf-8')]['albums'][-1]['total_tracks'] = g['tracks']['total']
					out[j.encode('utf-8')]['albums'][-1]['name'] = g['name']
					out[j.encode('utf-8')]['albums'][-1]['uri'] = g['uri']
					out[j.encode('utf-8')]['albums'][-1]['popularity'] = g['popularity']
					out[j.encode('utf-8')]['albums'][-1]['release_date'] = g['release_date']
					out[j.encode('utf-8')]['albums'][-1]['tracks'] = []
					for n in g['tracks']['items']:
						out[j.encode('utf-8')]['albums'][-1]['tracks'].append({})
						out[j.encode('utf-8')]['albums'][-1]['tracks'][-1]['duration'] = n['duration_ms']
						out[j.encode('utf-8')]['albums'][-1]['tracks'][-1]['name'] = n['name']
						out[j.encode('utf-8')]['albums'][-1]['tracks'][-1]['uri'] = n['uri']

			except:
				pass
			print out
			print "-----------------------------------------------"

	except:
		pass
