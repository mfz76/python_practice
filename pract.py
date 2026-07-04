# check whehter that nay number is negative or not

a,b,c,d,e = map(int, input("Enter the numbers(seperate them by spaces):").split(" "))

noneg = True

if a < 0 or b < 0 or c < 0 or d < 0 or e < 0:
    noneg = False

if noneg:
    print("there is not any negativen number.")
else:
    print("there is a negative numer.")








