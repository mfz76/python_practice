# find the most frequent word in a paragraph

x = """hey, my name is faraz, i am cse student here in india, i like to talk about myself,
    i like to talk but my wife doesn't allows me... """


y = x.split()
        

words = []
counts = []

for i in y:
    if i not in words:
        words.append(i)
        counts.append(y.count(i))


maximum = max(counts)
index = counts.index(maximum)

print(words[index])
print(counts[index])


