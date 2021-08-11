# Implementation of Chain Matrix Multiplication using Dynamic Programming
import sys

sol_matrix = [[-1 for _ in range(50)] for _ in range(50)]
 
def find_min(p, i, j):
    if(i == j):
        return 0
     
    if(sol_matrix[i][j] != -1):
        return sol_matrix[i][j]
     
    sol_matrix[i][j] = sys.maxsize
     
    for k in range(i,j):
        sol_matrix[i][j] = min(sol_matrix[i][j], find_min(p, i, k) + find_min(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
     
    return sol_matrix[i][j]
 
def Matrix_chain_multiplication(p,n):
    i = 1
    j = n - 1   
    return find_min(p, i, j)

print("Enter the dimension array :",end=' ')
arr = input().strip().split()
arr=list(map(int, arr))
n = len(arr)
print("Minimum number of multiplications required are ",Matrix_chain_multiplication(arr, n))
