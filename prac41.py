# Compress a string by counting consecutive repeated characters.

x = "aaabbccc"

result = ""
y = []

for i in range(len(x)):
    if x[i] not in y:
        if x.count(x[i]) > 1:
            result +=  str(x[i]) + str(x.count(x[i]))
            y.append(x[i])

     