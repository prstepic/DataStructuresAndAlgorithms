class Node:
  def __init__(self, value=0, nextNode=None):
    self.value = value
    self.nextNode = nextNode
  
  def setValue(self, value):
    self.value = value

  def setNextNode(self, nextNode):
    self.nextNode = nextNode

def addLists(headOne, headTwo):
  newHead = None
  currentNode = newHead
  carry = 0
  if(headOne == None and headTwo == None):
    return -1
  while(headOne != None and headTwo != None):
    sumOfNodes = headOne.value + headTwo.value + carry
    if(sumOfNodes > 10):
      if(newHead == None):
        newHead = Node(sumOfNodes - 10)
        currentNode = newHead
      else:
        currentNode.nextNode = Node(sumOfNodes - 10)
        currentNode = currentNode.nextNode
      carry = 1
    else:
      if(newHead == None):
        newHead = Node(sumOfNodes)
        currentNode = newHead
      else:
        currentNode.nextNode = Node(sumOfNodes)
        currentNode = currentNode.nextNode
      carry = 0

    headOne = headOne.nextNode
    headTwo = headTwo.nextNode

  if(headOne != None):
    while(headOne != None):
      sumOfNodes = headOne.value + carry
      if(sumOfNodes > 10):
        currentNode.nextNode = Node(sumOfNodes - 10)
        currentNode = currentNode.nextNode
        carry = 1
      else: 
        currentNode.nextNode = Node(sumOfNodes)
        currentNode = currentNode.nextNode
        carry = 0
      headOne = headOne.nextNode
  elif(headTwo != None):
    while(headTwo != None):
      sumOfNodes = headTwo.value + carry
      if(sumOfNodes > 10):
        currentNode.nextNode = Node(sumOfNodes - 10)
        currentNode = currentNode.nextNode
        carry = 1
      else: 
        currentNode.nextNode = Node(sumOfNodes)
        currentNode = currentNode.nextNode
        carry = 0
      headTwo = headTwo.nextNode
  return newHead

node1 = Node(7)
node2 = Node(1)
node3 = Node(6)
node4 = Node(5)
node5 = Node(9)
node6 = Node(2)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node5.nextNode = node6

testOutput = addLists(node1, node5)

while(testOutput != None):
  print(testOutput.value)
  testOutput = testOutput.nextNode

