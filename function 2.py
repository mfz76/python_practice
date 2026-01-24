# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 18:50:36 2026

@author: MOHAMMAD FARAZ
"""

def div_by(n,d):
    
    if d%n == 0:
        return True
    elif n<0 or d<0:
        print("Invalid Input")
    else :
        return False
    
hello = div_by(2,10)
print(hello)