# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:27:43 2026

@author: MOHAMMAD FARAZ
"""

import turtle
bob = turtle.Turtle()
print(bob)
'''bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)'''


for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()


