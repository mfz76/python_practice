#print natural numbers upto n
while True:
   try:
      x = int(input("Enter the number till which you wanna have a print:"))
      break

   except ValueError:
          print("invalid input")
         

for i in range(1,x+1):
  print(i)