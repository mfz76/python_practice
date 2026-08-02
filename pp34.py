# replace all  spaces from the string without using .replace()


x = input("Enter the string?").strip()


result = ""

for ch in x:
    if ch != " ":
        result += ch

print(result)


