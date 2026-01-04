# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 23:30:20 2026

@author: MOHAMMAD FARAZ
"""

password = input("Enter a password: ")

if len(password) < 8:
    print("Weak password (too short)")
elif password.isalpha():
    print("Add some numbers or symbols")
elif password.isdigit():
    print("Add some letters")
else:
    print("Strong password 💪")