# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 15:50:29 2026

@author: MOHAMMAD FARAZ
"""
n = 0
where = input("choose left or right ? ").strip().lower()

while where != "left":
    if where == "right":
        n += 1
        if n > 2:
            print(":))")
    else:
        print("invalid input")

    where = input("choose left or right ? ").strip().lower()
    
print("out")

                 