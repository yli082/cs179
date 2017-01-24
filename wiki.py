import wikipedia, sys

w = wikipedia.WikipediaPage(title="List of musicians")

for i in w.links:
	p = wikipedia.WikipediaPage(title=i)
	for j in p.links:
		out = {}
		out[j.encode('utf-8')] = ''
		try:
			a = wikipedia.WikipediaPage(title=j)
			html = a.html()
			start = html.find('<th scope="row">Born</th>')
			if start == -1:
				start = html.find('<th scope="row">Origin</th>')
			if start == -1:
				pass
			else:
				end = html[start:].find('</td>')
				end += start
				chunk = html[start:end]
				origin = ""
				while chunk.find('<a ') != -1:
					fake_start = chunk.find('title="')
					start = chunk[fake_start+7:].find('>')
					start += 7
					end = chunk[fake_start+2:].find('<')
					start += fake_start+1
					end += fake_start+2
					if origin == "":
						origin += chunk[start: end].encode('utf-8')
					else:
						origin = origin + ' ' + chunk[start: end].encode('utf-8')
					chunk = chunk[end+1:]
				out[j.encode('utf-8')]= origin
		except:
			pass
		print out
