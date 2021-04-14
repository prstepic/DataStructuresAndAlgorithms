class Node:
  def __init__(self, value=0, nextNode=None):
    self.value = value
    self.nextNode = nextNode
  
  def setValue(self, value):
    self.value = value

  def setNextNode(self, nextNode):
    self.nextNode = nextNode

# Brute Force O(nm) runtime, O(1) space
# n is the length of node1's list
# m is the length of node2's list
def bfFindIntersection(node1, node2):
  if(node1 == None or node2 == None):
    return False
  else:
    currentNode = node2
    while(node1 != None):
      currentNode = node2
      while(currentNode != None):
        if(node1 == currentNode):
          return node1
        else:
          currentNode = currentNode.nextNode
      node1 = node1.nextNode

# HashMap O(n + m) runtime, O(n) space
# n is the length of node1's list
# m is the length of node2's list
def hmFindIntersection(node1, node2):
  if(node1 == None or node2 == None):
    return False
  setOfMem = set()
  while(node1 != None):
    setOfMem.add(id(node1))
    node1 = node1.nextNode
  while(node2 != None):
    if(id(node2) in setOfMem):
      return node2
    else:
      node2 = node2.nextNode
  return False
  
# non HashMap O(n + m) runtime, O(1) space
# n is the length of node1's list
# m is the length of node2's list
def cmFindIntersection(node1, node2):
  if(node1 == None or node1 == None):
    return False
  lengthL1 = 0
  lengthL2 = 0
  currentNode1 = node1
  currentNode2 = node2
  while(currentNode1.nextNode != None):
    currentNode1 = currentNode1.nextNode
    lengthL1 += 1
  while(currentNode2.nextNode != None):
    currentNode2 = currentNode2.nextNode
    lengthL2 += 1
  if(currentNode1 != currentNode2):
    return False
  else:
    if(lengthL1 == lengthL2):
      for i in range(0, lengthL1):
        if(node1 == node2):
          return node1
        else:
          node1 = node1.nextNode
          node2 = node2.nextNode
    elif(lengthL1 < lengthL2):
      for i in range(0, lengthL2 - lengthL1):
        node2 = node2.nextNode
      for i in range(0, lengthL1 + 1):
        if(node1 == node2):
          return node1
        else:
          node1 = node1.nextNode
          node2 = node2.nextNode
    else:
      for i in range(0, lengthL1 - lengthL2):
        node1 = node1.nextNode
      for i in range(0, lengthL2 + 1):
        if(node1 == node2):
          return node1
        else:
          node1 = node1.nextNode
          node2 = node2.nextNode
    return False