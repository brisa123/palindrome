import os

a=int(input("enter any number"))

if a>1:
    for x in range(2,a):
        if a%x==0:
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not prime")