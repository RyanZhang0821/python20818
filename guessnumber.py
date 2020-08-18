# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:59:50 2020

@author: user
"""

import random
num=random.randint(1,10)
i=0
while i<5:
    ans=int(input("Type number:"))
    if ans==num:
        print("right")
        break
    elif i>ans:
        print("bigger")
        i = i + 1
    elif i<ans:
        print("smaller")
        i = i + 1
    else:
        print("wrong")
while i<=5:
    print("You tried",i,"times")
    break
