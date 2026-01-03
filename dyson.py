# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 15:44:38 2026

@author: MOHAMMAD FARAZ
"""

x = input("Enter a String:")
y = input("Enter the character:")

count   = 0

for c in x:
    if (c == y):
        count += 1
        
print("Count:",count)
        