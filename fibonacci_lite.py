n,a,b= int(input()),0,1
while n!=0:
    a,b = b,a+b
    n-=1
print(a)
