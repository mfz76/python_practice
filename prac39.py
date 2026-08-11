# remove duplicate characters from a string while maintaining the original order 

s = "Hello, how are you?"

result = ""

for ch in s:
    if ch not in result:
        result += ch


print(result)
     
