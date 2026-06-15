# smallest of all the digits from a given number

x = str(abs(int(input("Enter the Desire number:"))))

smallest = int(x[0])

for value in x:
    if int(value) < smallest:
        smallest = int(value)
        
print(smallest)