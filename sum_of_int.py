#sum of Integers
#Using built-in function sum()

#def even_better(n):
   # return sum(range(n + 1))

num=int(input("enter a number"))

def add_it_up(x):
    res = 0
    if x<0:
        return 0
    else:
        for i in range(x+1):
            res=i+res
    return res


sum=add_it_up(num)
print(sum)
