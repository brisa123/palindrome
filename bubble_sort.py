import os
import sys

a=[32,45,1,5,66,89,3,10,5]

def bs(a):
    b=len(a)-1

    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a
bs(a)
print(a)