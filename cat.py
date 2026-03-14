# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:22:22 2026

@author: MOHAMMAD FARAZ
"""

def print_twice(bruce):
    print(bruce)
    print(bruce)
    cat_twice()
    
    
def cat_twice(part1,part2):
    cat = part1 + part2
    print_twice(cat)
    
cat_twice("hello", " hi")
cat_twice(45,23)