class GraphNode:
  def __init__(self, value=0):
    self.children = []
    self.value = value

class Graph:
  def __init__(self):
    self.nodes = []
    self.visited = set()
  
  def rootBFS(self):
    if(len(self.nodes) != 0):
      self.breadthFirstSearch(self.nodes[0])
    else:
      return False
    self.visited.clear()
  
  def rootDFS(self):
    if(len(self.nodes) != 0):
      self.depthFirstSearch(self.nodes[0])
    else:
      return False
    self.visited.clear()

  def depthFirstSearch(self, node):
    if(isinstance(node, GraphNode) == False or node == None):
      return False
    else:
      self.visited.add(node)
      print(node.value)
      for child in node.children:
        if(child not in self.visited):
          self.depthFirstSearch(child)

  def breadthFirstSearch(self, node):
    if(isinstance(node, GraphNode) == False or node == None):
      return False
    else:
      nodeQueue = []
      nodeQueue.append(node)
      accountedFor = set()
      while(len(nodeQueue) != 0):
        tempNode = nodeQueue.pop(0)
        self.visited.add(tempNode)
        print(tempNode.value)
        for child in tempNode.children:
          if(child not in self.visited and child not in accountedFor):
            nodeQueue.append(child)
            accountedFor.add(child)
    self.visited.clear()

  def topologicalSort(self):
    orderOfSort = []
    processQueue = []
    inboundCounts = {}
    for node in self.nodes:
      if(node not in inboundCounts):
        inboundCounts[node] = 0
      for child in node.children:
        if(child not in inboundCounts):
          inboundCounts[child] = 1
        else:
          inboundCounts[child] += 1
    for key, value in inboundCounts.items():
      if(value == 0):
        processQueue.append(key)
    while(len(processQueue) != 0):
      tempNode = processQueue.pop(0)
      for child in tempNode.children:
        inboundCounts[child] -= 1
        if(inboundCounts[child] == 0):
          processQueue.append(child)
      orderOfSort.append(tempNode)
    if(len(orderOfSort) == len(self.nodes)):
      return orderOfSort
    else:
      return False
