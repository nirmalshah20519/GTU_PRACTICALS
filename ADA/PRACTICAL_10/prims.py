from math import *
from networkx import *
from numpy import *

N = 5
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
selected_node = [0, 0, 0, 0, 0]
no_edge = 0
selected_node[0] = True
print(" Edge   : Minimal Weight")
while (no_edge < N - 1):
    minimum = inf
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n

    selected_node[b] = True
    no_edge += 1