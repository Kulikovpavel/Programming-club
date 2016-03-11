from lxml import html
import requests
import codecs


home = 'http://gatn.mosreg.ru'
links = []
pics = []
items = []
for i in range(1, 8):

	page = requests.get(home + '/multimedia/novosti/novosti/?PAGEN_1=%s'%i)
	tree = html.fromstring(page.content)

	links_current = tree.xpath('//div[@class="news-item"]/a[@class="link"]/@href')
	pics_current = tree.xpath('//div[@class="news-item"]/a[@class="link"]/div[@class="pic"]/img/@src') 
	items_current = tree.xpath('//div[@class="news-item"]/a[@class="link"]/div[@class="title"]/text()')

	links.extend(home + s.strip(' \t\n\r') for s in links_current)
	pics.extend(home + s.strip(' \t\n\r') for s in pics_current)
	items.extend(items_current)


zipped = zip(links, pics, items)

with codecs.open('out.txt','w',encoding='utf8') as f:
	for e in zipped:
		f.write('<p><a href="%s"><img src="%s"/><span style="margin-left: 5px;">%s</span></a></p>' % e)
		f.write('\n')
