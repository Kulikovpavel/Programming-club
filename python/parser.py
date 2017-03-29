from lxml import html
import requests
import codecs
import json
from lxml import objectify
from datetime import datetime


home = 'http://gatn.mosreg.ru'
links = []
pics = []
items = []
texts = []
for i in range(5, 0, -1):

	page = requests.get(home + '/sobytiya/novosti_ministerstva/?page=%s'%i)
	tree = html.fromstring(page.content)

	links_current = tree.xpath('//div[@class="event__content"]/h3[@class="event__title"]/a/@href')
	pics_current = tree.xpath('//div[@class="event__image-wrap"]/a[@class="event__image-link"]/img/@src')
	items_current = tree.xpath('//div[@class="event__content"]/h3/a/text()')

	links.extend(home + s.strip(' \t\n\r') for s in links_current)
	pics.extend(home + s.strip(' \t\n\r') for s in pics_current)
	items.extend(items_current)

	# print(items_current)

	for elem in links_current:
		page = requests.get(home + elem)
		tree = html.fromstring(page.content)
		text = tree.xpath('//div[@class="article__inner  typical"]/p')
		p_array = [html.tostring(elem, encoding='unicode', pretty_print=True) for elem in text]
		p_string = "".join(p_array)
		date = datetime.now().strftime('%d.%m.%Y')
		texts.append(p_string + "<p>Добавлено %s</p>" % date)



	print(i)


zipped = list(zip(links, pics, items, texts))

with codecs.open('out1.txt','w',encoding='utf8') as f:
	f.write(json.dumps(zipped))

	# for e in zipped:
	# 	string = '<p><a href="%s"><img src="%s"/><span style="margin-left: 5px;">%s</span></a></p><div>%s</div>' % e

	# 	f.write(json.dumps([string]))
	# 	f.write('\n')
