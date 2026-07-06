# check if the number is prime or not

while True:
    try:
        x = int(input("Enter the number:"))
        if x <= 1 :
            print("invalid input!")
            continue
        break
    except Exception:
        print("invalid input!")

is_prime = True

for i in range(2,x):
    if x % i != 0:
        is_prime = False
        break

if is_prime:
    print("its  a prime number")
else:
    print("its not a prime number")
