# check any number is even or not out of taken 5 numbers



a,b,c,d,e = map(int,input("Enter the numbers(separate them by comma):").split(","))

noteven = True

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0 or d % 2 == 0 or e % 2 == 0:
    noteven = False

if noteven:
    print("not any even")
else:
    print("there is an even number")




