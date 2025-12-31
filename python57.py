# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 23:19:39 2025

@author: MOHAMMAD FARAZ
"""

text = input("Enter a string: ")
char_to_count = input("Enter the character to count: ").strip()

# Initialize counter
count = 0

# Loop through each character in the string
for ch in text:
    if ch == char_to_count:
        count += 1

# Print the result
print(f"The character '{char_to_count}' appears {count} times.")
