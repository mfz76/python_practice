#reverse for loop from n to 1
while True:
    try:
        x = int(input("Enter the number:"))
        break
    except Exception:
        print("invalid input")

for i in range(x+1,0,-1):
    print(i)






