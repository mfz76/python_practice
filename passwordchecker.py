# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 22:09:02 2026

@author: MOHAMMAD FARAZ
"""

x = input("Enter the Password:\n")
y = len(x)
if  (y < 6):
    print("Weak")
elif (y>=6 and y<=10):
    print("MEDIUM")
else:
    print("Strong")
    