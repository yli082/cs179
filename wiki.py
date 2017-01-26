import wikipedia, sys

w = wikipedia.WikipediaPage(title="List of musicians")

for i in w.links:
	p = wikipedia.WikipediaPage(title=i)
	for j in p.links:
		print j.encode('utf-8')
		out = {}
		out[j.encode('utf-8')] = ''
		try:
			a = wikipedia.WikipediaPage(title="weezer")
			summary = a.summary
			content = a.content
			ref = a.references
			out[j.encode('utf-8')] = {}
			out[j.encode('utf-8')]["summary"] = summary 
			out[j.encode('utf-8')]["content"] = content
			out[j.encode('utf-8')]["references"] = ref
			
		except:
			pass
		print out
		print "-----------------------------------------------"
		sys.exit()
