# count the number of vowel and consonants in a string 

x = "Batman"

count = 0

for ch in x:
    if ch in "aeiou":
        count += 1
    
print("vowels are",count)
print("consonants are",len(x)-count)