# iterative factorial progam.

from time import *

N=int(input("Enter the number :"))
x=time()
fact = 1
i = N
while i != 0 :
    fact = fact * i
    i -= 1
print("RESULT :-")
print(N,"! = ",fact)
print("Time taken : ",(time()-x),"sec")