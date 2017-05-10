#!/usr/bin/env python3

import numpy as np
#This is a short python program to compute 
#The sum of all the multiples of 3 or 5 below 1000

#define our constant 1000:
n=1000

#Now we need to find all the multiples of 3 and 5 below n:
def mul(n,num):
    a=np.array([num])
    for i in range(2,n-1):
        m=num*i
        if(m<n):
            a=np.append(a,[m])
    return a

three=set(mul(n,3))
five=set(mul(n,5))
m=np.asarray(list(three|five))
print(np.sum(m))
