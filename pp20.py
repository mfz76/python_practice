#given a list of numbers find all the paits that sums to a target

a = [1,2,3,4,5]
b = a

total = 0

pairs = []

for i in range(len(a)):
    for j in range(len(b)):
        total = a[i] + b[j]
        if total == 5:
            pairs.append((a[i],b[j]))

print(pairs)