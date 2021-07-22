# Implementation of DFS in python

graph = {
  'Apple' : ['Box','Card'],
  'Box' : ['Apple', 'Dust', 'Egg'],
  'Card' : ['Apple', 'Flower'],
  'Dust' : ['Box'],
  'Egg' : ['Box', 'Flower'],
  'Flower' : ['Card', 'Egg']
}

def dfs(stack, graph, node):
    if node not in stack:
        print (node, end=" --> ")
        stack.append(node)
        for neighbour in graph[node]:
            dfs(stack, graph, neighbour)

stack = []
print(graph.keys())
node = str(input("Enter the node from above list you wants to search : "))
dfs(stack, graph, node)