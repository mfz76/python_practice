# sum of the digit of a number using while loop

x = int(input("Enter the number:"))

total = 0


while x > 0:
    digit = x % 10 
    total = total + digit
    x = x // 10

print(total)
