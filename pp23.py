# to reverse a string without using slicing or reverse()

x = "Faraz"

char = ""

for i in range(len(x)-1,-1,-1):
    char += x[i]

print(char)