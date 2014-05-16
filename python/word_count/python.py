with open('book1.txt', 'r', encoding='utf-8') as file:
	lines = file.readlines()
	
	dict = {}
	for elem in lines:
		words = elem.lower().replace(".", "").replace(",", "").replace(";", "").replace(":", "").replace("-", "").split(" ")
		for word in words:
			#if word == '\n': continue
			if word in dict:
				dict[word] += 1
			else: 
				dict[word] = 1

	with open('output.txt', 'w', encoding='utf-8') as file:
		for w in sorted(dict, key=dict.get, reverse=True):  #получаем сортированный по значению список ключей, после чего записываем в файл
			file.write('%s %s\n' % (w, dict[w]))
		 
