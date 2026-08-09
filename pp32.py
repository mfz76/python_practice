# count the concurreny of a selected character without using .count 

x = input("Enter the string:")
y = input("Enter the character you wanna count : ")



count = 0


for ch in x:
    if ch == y:
        count += 1

print(count) 