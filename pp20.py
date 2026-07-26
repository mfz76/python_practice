# to check whether the string is palindrome or not


# Check whether a string is a palindrome

text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
text = text.lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")