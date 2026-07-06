#count the number of digits in a number without converting it into strings
while True:
    try:
        x = abs(int(input("Enter the number:")))
        break
    except Exception :
        print("Invalid Input!")

count  = 0


if x == 0:
    count  = 1

while x > 0:
    count += 1
    x  = x // 10
 

print(count)