#!/usr/bin/env python3

import numpy as np
#This is to solve the second problem on Project Euler
#We will start by creating a fibonacci number generator

#Let's start by finding the nth fibonacci number:
#We will also use dynamic programming table:
fibTable=np.asarray([[1,1.0],[2,1.0]])
#print(fibTable.size)
#print(fibTable)
def fib(n):
    global fibTable
    if(n==1 or n==2):
        return fibTable[1][1]
    else:
        if((fibTable.size)/2==(n-1)):
            #That means fib(n-2) and fib(n-1) exists already
            fib2=fibTable[n-3][1]
            fib1=fibTable[n-2][1]
            fibTable=np.append(fibTable,[n,fib1+fib2])
            fibTable=np.reshape(fibTable,(-1,2))
            return fib1+fib2
        elif((fibTable.size)/2==(n-2)):
            #That means fib(n-2) exits and not fib n-1)
            fib2=fibTable[n-3][1]
            fib1=fib(n-1)
            fibTable=np.append(fibTable,[n,fib1+fib2])
            fibTable=np.reshape(fibTable,(-1,2))
            return (fib1+fib2)
        else:
            fib2=fib(n-2)
            fib1=fib(n-1)
            fibTable=np.append(fibTable,[n,fib1+fib2])
            fibTable=np.reshape(fibTable,(-1,2))
            return (fib1+fib2)

n=int(input("Enter a number "))

print("The ", n, "th fibonacci number is: ", fib(n) )
print(fibTable)

sum=0
for i in fibTable:
    if(i[1]<4000000 and np.mod(i[1],2)==0):
        sum=sum+i[1]

print(sum)
