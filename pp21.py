# find the nth prime number 


from sympy import prime

while True:
    try: 
        x = int(input("Enter the number:"))
        if x <= 0:
            print("Invalid input!")
            continue
        break
    except ValurError:
        print("Invalid Input!")


print(prime(x))