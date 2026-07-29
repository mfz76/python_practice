# check if a string has all unique characters without using any data structure


x = "Faraz"

flag = True

for ch in x:
    if ch in x.replace(ch,"",1):
        flag = False

if flag:
    print("thus, all are unique")
else:
    print("all, are not unique") 