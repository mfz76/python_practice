# find the first non - repeating character of the string.

x = "hello"

for ch in x:
    if x.count(ch) == 1:
        print(ch)
        break