#!/usr/bin/env python3
import numpy as np
import math

n=int(input("Enter a number: "))

def div(a,b):
    if (np.mod(a,b)==0):
        return True
    else:
        return False

def divisor(n):
    a=np.array([1])
    for i in range(2,int(math.sqrt(n))):
        if(div(n,i)):
            a=np.append(a,[i,n/i])
    return a

#The amical number is the sum of all the proper divisor
def Amical(n):
    a=divisor(n)
    b=np.sum(a)
    c=divisor(b)
    #edge case:
    if(b==n):
        return 0
    elif(np.sum(c) == n):
        return b
    else:
       # print(n," does not have amical number")
        return 0

#print(divisor(496))
#print(sum(divisor(496)))
#print(Amical(496))

#Now to find the sum of all amicable numbers under 10000:
def sumOfA(n):
    amical=np.array([220,284])
    i=285
    while(i<n):
        j=Amical(i)
        if(j!=0):
           amical=np.append(amical,[i,j])
           i=j+1
        else:
            i=i+1


    return amical

a=sumOfA(n)
print(a)
print(np.sum(a))
