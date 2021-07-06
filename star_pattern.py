import os

def pattern(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))

pattern(5)