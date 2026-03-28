# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 23:35:21 2026

@author: MOHAMMAD FARAZ
"""

# so its a number guessing game from where we gonna start out journey to become the best out there in tech.

import random

x = random.randint(1,100)


while True:
    try:
       y = int(input("Guess the number (1-100): "))
    except:
        print("Enter error value.\n")
        
    if y<1 and y>100:
        print("enter the number in range.")
        continue 
    diff = abs(x-y)
    
    if x == y:
        print(f"🔥 You got it!, its {x}\n")
        break
    elif y > x :
        if diff <= 10:
           print("high!\n")
        else:
           print("very high\n")
    elif y < x:
        if diff<=10:
           print("low!\n")
        else:
           print("very low\n")
    else:
        print("INVALID INPUT\n")
    
        
