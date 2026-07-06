#check a number is number palindrome without converting it into string

while True:
    try:
        x = int(input("Enter the number:"))
        if     9 >=  x  >= -9:
            print("Invalid Input!")
            continue
        break
    except Exception:
        print("Invalid Input!")

if x < 0:
    temp1 = abs(x)
else:
    temp1 = x


rev = 0

while temp1 > 0:
   digit = temp1 % 10 
   rev = rev * 10 + digit
   temp1 = temp1 // 10


if x < 0 :
 temp2  =   -rev


if x < 0:
    if temp2 == x:
        print("its a palindrome")
    else:
        print("its not a palindrome")
elif x > 0:
    if rev == x:
        print("its a palindrome")
    else:
        print("its not a palindrome")