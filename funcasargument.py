# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:44:03 2026

@author: MOHAMMAD FARAZ
"""

def do_twice(f,value):
    f(value)
    f(value)
def print_spam(inputs):
    print("spam")
    print(inputs)
    
do_twice(print_spam,35)