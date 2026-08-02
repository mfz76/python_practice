# print the longest word in a sentence

x  = "hello how are you ?"


words = x.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

