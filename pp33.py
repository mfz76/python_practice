# remove spaces from a string with using .replace()

x = input("Enter the String:").strip()

result = ""

if " " in x:
    result += x.replace(" ","",len(x))
else:
    result = x

print(result)