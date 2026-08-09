 # reverse each word in senetence but keep the  word order


x = input("Enter the string:")


hold = x.split()

for i in range(len(hold)):
    ok = "".join(reversed(hold[i]))
    print(ok, end = " ")