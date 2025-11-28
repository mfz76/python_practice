# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 13:29:37 2025

@author: MOHAMMAD FARAZ
"""

num = int(input("Enter the guessed number:"))

if num%2==0:
    print("even")
else:
    print("odd")
    

if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("its zero")