# find and print all prime numbers between 1 and n 

while True:
    try:
        x = int(input("Enter the number:"))
        if x<=1:
            print("invalid input")
            continue
        if x == 2:
            print("There is no prime number between 1 and 2, since 2 is the smallest prime number.")
        break
    except Exception:
        print("Invalid Input!")


for i in range(2,x):
    
    is_prime = True

    for j in range(2,i):
        if  i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{i} is a prime number.")
    


