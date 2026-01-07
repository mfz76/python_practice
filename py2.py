'''secret = 234
X = int(input("Enter the secret passkey you wanna enter:"))
if X < secret :
    print("too low")
elif X > secret :
    print("too high")
else :
    print("matched")'''
'''while True:
    print("yes")'''

'''n = 0
where = input("You are lost in the woods,where do you wanna go now? ")
while where == "right":
    n = n + 1
    if n>2:
        print(":(")
    where = input("You are lost in the woods,where do you wanna go now?")
print("you got out!")'''

'''n = 0
while n < 5:
   print(n)
   n=n+1'''

'''for n in range(5):
    print(n)'''

mysum = 0
start  = 3
end = 5
for i in range (start,end+1):
    print("i=",i)
    mysum += i
    print(mysum)
    
  