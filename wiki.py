import wikipedia

w = wikipedia.WikipediaPage(title="List of musicians")

for i in w.links:
	p = wikipedia.WikipediaPage(title=i)
	for j in p.links:
		print j.encode('utf-8')
