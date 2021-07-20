# Recursive Factorial Program using Python

from time import *

def fact(N):
    n = int(N)
    if n == 1:
        return 1
    else :
        return n * fact(n-1)

N = int(input("enter the number : "))
x=time()
res = fact(N)
print(N,"! = ",res)
print("Time taken : ",(time()-x),"sec")