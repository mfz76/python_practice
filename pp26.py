# find the frequency of each character in a string

x = "hello"


seen = []

for ch in x:
    if ch not in seen:
       count = 0
       for  i in range(len(x)) :
           if ch == x[i]:
               count += 1
       print(f"{ch} is only {count}")
       seen.append(ch)