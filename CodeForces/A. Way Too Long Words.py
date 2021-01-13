n = int(input())
words = [input() for i in range(n)]

for word in words:
    if len(word)>10:
        words[words.index(word)] = word[0]+str(len(word)-2)+word[-1]

for word in words:
    print(word)