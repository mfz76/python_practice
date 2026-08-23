# check if one string is rotation of the other

x = "faraz"

y = "azar"

if len(x) == len(y) and y in ( x + x ):
    print("True")
else:
    print("False")
   