# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 22:09:43 2026

@author: MOHAMMAD FARAZ
"""

s = "abbsfsvdb"
seen = ""
for char in s:
    if char  not in seen:
        seen = seen + char 
print(seen)
print(len(seen))