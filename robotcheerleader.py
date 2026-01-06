# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 21:06:32 2026

@author: MOHAMMAD FARAZ
"""

lettersdump = "a,e,i,o,u,A,E,I,O,U"

word = input("Enter the word to chear for:")
x = int(input("Curiosity level:"))

for c in word:
    if (c in lettersdump):
        print(f"Give me an {c}:{c}")
    else:
        print(f"Give me a {c}:{c}")
print("What does that spells!!!")
for i in range(x):
    print(word)


