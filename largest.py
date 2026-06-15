# to print the largest digit out of all from a given number

x = str(abs(int(input("Enter the Desired number:").strip())))

largest = int(x[0])

for value in x:
    if int(value)  >  largest:
        largest = int(value)
      
print(largest) 