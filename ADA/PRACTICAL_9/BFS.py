# Implementation of BFS in python

graph = {
  'Apple' : ['Box','Card'],
  'Box' : ['Apple', 'Dust', 'Egg'],
  'Card' : ['Apple', 'Flower'],
  'Dust' : ['Box'],
  'Egg' : ['Box', 'Flower'],
  'Flower' : ['Card', 'Egg']
}

visited = []   #List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " --> ")
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print(graph.keys())
node = str(input("Enter the node from above list you wants to search : "))
bfs(visited, graph, node)