#accept an integer and chekc whether its an even or odd
while True:
   try:
       x = int(input("Enter the number:"))
       break
   except Exception:
       print("invalid input, try again bro!!:(")


if x % 2 == 0:
    print("its even")

else:
    print("its an odd")