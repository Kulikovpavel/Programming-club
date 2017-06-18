import sys


in_file = sys.stdin.readlines()

current_word = None
current_list = None
word = None
result = list()

for line in in_file:
    word, filename = line[:-1].split('\t')  # \n at the end of each line, remove it
    if current_word != word:
        current_list = list()
        current_word = word
        result.append((word, current_list))

    current_list.append(filename)


for line in result:
    print(line[0] + '\t' + str(line[1]))
