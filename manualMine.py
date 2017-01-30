from bs4 import BeautifulSoup
import wikipedia, spotipy, json, pprint, sys, urllib2

sp = spotipy.Spotify()
pp = pprint.PrettyPrinter(indent=4)
listOfStuff = []

def find_lists_of_musicians(element):
	for li in element.findAll('li'):
		s_li = str(li)
		if "<li><a" in s_li:
			for x in s_li.split('"'):
				if x.startswith('/wiki'):
					if x not in listOfStuff:
						listOfStuff.append(x)
					break
	for tr in element.findAll('tr'):
		s_tr = str(tr)
		if "<td><a" in s_tr:
			for x in s_tr.split('"'):
				if x.startswith('/wiki'):
					if x not in listOfStuff:
						listOfStuff.append(x)
					break

url = "https://en.wikipedia.org/wiki/List_of_musicians"
f = urllib2.urlopen(url)
html = f.read()
o = BeautifulSoup(html, 'html.parser')
find_lists_of_musicians(o)
i = 0
output = {}
while i < len(listOfStuff):
	if ("list of" in listOfStuff[i].lower() or "list_of" in listOfStuff[i].lower() 
		or "lists of" in listOfStuff[i].lower() or "lists_of" in listOfStuff[i].lower()
		or "musicians" in listOfStuff[i].lower()
		or "bands" in listOfStuff[i].lower() or "groups" in listOfStuff[i].lower()):
		url = "https://en.wikipedia.org" + listOfStuff[i]
		f = urllib2.urlopen(url)
		html = f.read()
		o = BeautifulSoup(html, 'html.parser')
		find_lists_of_musicians(o)
	else:
		text = listOfStuff[i].replace('_', ' ')
		text = text.replace('/wiki/', '')
		text = urllib2.unquote(text)
		
		output[text] = {}
		try:
			results = sp.search(q='artist:'+text, type='artist')
			uri = results['artists']['items'][0]['uri']
			name = results['artists']['items'][0]['name']
			
			artistPage = wikipedia.WikipediaPage(title=text)
			
			summary = artistPage.summary
			content = artistPage.content
			ref = artistPage.references
			
			output[text]['summary'] = summary
			output[text]['content'] = content
			output[text]['references'] = ref
			output[text]['albums'] = []
			output[text]['genres'] = results['artists']['items'][0]['genres']
			output[text]['followers'] = results['artists']['items'][0]['followers']['total']
			output[text]['popularity'] = results['artists']['items'][0]['popularity']
			
			results = sp.artist_albums(uri, album_type='album')

			album_uris = []
			for m in results['items']:
				album_uris.append(m['uri'])

			results = sp.albums(album_uris)

			track_uris = []
			for g in results['albums']:
				output[text]['albums'].append({})
				output[text]['albums'][-1]['total_tracks'] = g['tracks']['total']
				output[text]['albums'][-1]['name'] = g['name']
				output[text]['albums'][-1]['uri'] = g['uri']
				output[text]['albums'][-1]['popularity'] = g['popularity']
				output[text]['albums'][-1]['release_date'] = g['release_date']
				output[text]['albums'][-1]['tracks'] = []
				for n in g['tracks']['items']:
					output[text]['albums'][-1]['tracks'].append({})
					output[text]['albums'][-1]['tracks'][-1]['duration'] = n['duration_ms']
					output[text]['albums'][-1]['tracks'][-1]['name'] = n['name']
					output[text]['albums'][-1]['tracks'][-1]['uri'] = n['uri']
		except:
			pass
		print output

	i += 1
