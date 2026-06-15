# to print only odd digits of a given number

x = str(abs(int(input("Enter the number:").strip())))

for value in x:
    if int(value) % 2 != 0:
        print(value)