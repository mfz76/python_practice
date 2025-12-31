# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 23:35:08 2025

@author: MOHAMMAD FARAZ
"""

# Get input from user
n = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Loop from 1 to n
for i in range(1, n + 1):
    factorial *= i  # multiply factorial by i

# Print result
print(f"The factorial of {n} is {factorial}")
