# to check that if a string is palindrome or not using three ways: indexing, reverse() and slicing

# by indexing
'''
x = "mom"

rev = ""

for i in range(len(x)-1,-1,-1):
    rev += x[i]

if x == rev:
    print("it's palindrome.")
else:
    print("it's not a palindrome.")
'''
# by slicing 
'''

x = "mom"

if x == x[::-1]:
    print("it's a palindrome.")
else:
    print("it's not a palindrome.")

    '''

# by reverse

x = "faraz"


if x == "".join(reversed(x)):
   print("it's palindrome")
else:
    print("it's not a palindrome.")