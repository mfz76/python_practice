# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:23:41 2026

@author: MOHAMMAD FARAZ
"""

for i  in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3== 0:
        print("fizz")
    elif i%5 == 0:
        print("Buzz")
    
    else:
        print(i)