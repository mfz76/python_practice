# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 22:40:10 2025

@author: MOHAMMAD FARAZ
"""
count = 0
x = input("Enter something!\n")
for ch in x:
    if ch in "aeiou":
        count =  count + 1
print(count)
