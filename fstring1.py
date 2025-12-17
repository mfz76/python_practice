# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 14:11:24 2025

@author: MOHAMMAD FARAZ
"""

#fstirngs

num = 3000
fraction = 1/3
#print(num*fraction,"is",fraction*100,"% of",num)

#print(num*fraction,"is",str(fraction*100)+"% of",num)
'''exactly what i wanted from the prev print statment,
concatenation has done it over here, it removed the space
between the numerical part and % sing.'''

#but the best out of all is f-strng :))
print(f"{num*fraction} is {fraction*100}% of {num}")