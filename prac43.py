# count words in sentence without using .split()


x = "what is Your name han?"

count = 0

for i in range(len(x)):
    if x[i] == " " :
        count += 1
        break

i = 1

for i in range(len(x)):   
    if x[i-1] == " ":
        count += 1
        

    
print(count)


