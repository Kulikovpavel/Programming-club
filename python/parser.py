from lxml import html
import requests
import codecs
import json
from lxml import objectify


home = 'http://gatn.mosreg.ru'
links = []
pics = []
items = []
texts = []
for i in range(5, 0, -1):

	page = requests.get(home + '/multimedia/novosti/novosti/?PAGEN_1=%s'%i)
	tree = html.fromstring(page.content)

	links_current = tree.xpath('//div[@class="news-item"]/a[@class="link"]/@href')
	pics_current = tree.xpath('//div[@class="news-item"]/a[@class="link"]/div[@class="pic"]/img/@src') 
	items_current = tree.xpath('//div[@class="news-item"]/a[@class="link"]/div[@class="title"]/text()')

	links.extend(home + s.strip(' \t\n\r') for s in links_current)
	pics.extend(home + s.strip(' \t\n\r') for s in pics_current)
	items.extend(items_current)



	for elem in links_current:
		page = requests.get(home + elem)
		tree = html.fromstring(page.content)
		text = tree.xpath('//div[@class="text"]/p')
		p_array = [html.tostring(elem, encoding='unicode', pretty_print=True) for elem in text]
		p_string = "".join(p_array)
		texts.append(p_string + "<p>Добавлено 27.04.2016</p>")
		


	print(i)


zipped = list(zip(links, pics, items, texts))

with codecs.open('out1.txt','w',encoding='utf8') as f:
	f.write(json.dumps(zipped))

	# for e in zipped:
	# 	string = '<p><a href="%s"><img src="%s"/><span style="margin-left: 5px;">%s</span></a></p><div>%s</div>' % e

	# 	f.write(json.dumps([string]))
	# 	f.write('\n')
