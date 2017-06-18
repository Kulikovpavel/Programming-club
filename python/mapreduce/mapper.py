import sys
in_file = sys.stdin.readlines()


data = map(lambda x: x.split('\t'), in_file)

for line in data:
    words = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line[1])).lower().split()

    for word in set(words):
        print(word + '\t' + line[0])
