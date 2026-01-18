# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 12:38:48 2026

@author: MOHAMMAD FARAZ
"""

found = False# found is flag here, flag doesnt mean anything its just  a variable.
secret = 100
for i in  range(1,11):
    if i == secret:
        print("found")
        found =  True
if (not found):
    print("not found")