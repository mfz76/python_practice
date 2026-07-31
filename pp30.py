# convert a string into upper without using upper

while True:
    x = input("Give the input: ")

    if x.isdigit():
        print("Invalid Input!")
    else:
        break

result = ""

for ch in x:
    if "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)