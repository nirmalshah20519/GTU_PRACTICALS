# Knapsack Problem using python language

def knapSack(W, wts, profit, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]  # Set all values of matrix with 0's
  
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0: 
                K[i][w] = 0         # Setting 1st row & col with 0's
                
            elif wts[i-1] <= w:                                                                
                K[i][w] = max(profit[i-1] + K[i-1][w-wts[i-1]],  K[i-1][w])
                
            else:
                K[i][w] = K[i-1][w]
  
    return K[n][W]       # return the value present at last row and last col of matrix
  
profit = [60, 100, 120]
wts = [10, 20, 30]
W = 50
n = len(profit)
print(knapSack(W, wts, profit, n))