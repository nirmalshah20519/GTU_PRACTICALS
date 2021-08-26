# Implementation of a Knapsack problem using greedy algorithm. 

def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_value = 0
    for i in index:
        if weight[i] <= capacity:
            max_value += value[i]
            capacity -= weight[i]
        else:
            max_value += value[i]*capacity/weight[i]
            break
    return max_value


print("Enter the values :",end=' ')
value = input().strip().split()
value=list(map(int, value))
n1 = len(value)

print("Enter the weights :",end=' ')
weight = input().strip().split()
weight=list(map(int, weight))
n2 = len(weight)

print("Enter the capacity :",end=' ')
capacity = int(input())

max_value = fractional_knapsack(value, weight, capacity)
print('The maximum value of items that can be carried:', max_value)