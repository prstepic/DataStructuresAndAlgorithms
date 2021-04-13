class Node:
  def __init__(self, value=0, nextNode=None):
    self.value = value
    self.nextNode = nextNode
  
  def setValue(self, value):
    self.value = value

  def setNextNode(self, nextNode):
    self.nextNode = nextNode

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  def addNode(self, nodeToAdd):
    if(self.head != None):
      self.tail.nextNode = nodeToAdd
      self.tail = nodeToAdd
    else:
      self.head = nodeToAdd
      self.tail = nodeToAdd
  def traverseList(self):
    if(self.head == None):
      print("[]")
      return -1
    else:
      currentNode = self.head
      while(currentNode != None):
        print(currentNode.value)
        currentNode = currentNode.nextNode

def partitionLL(head, partitionVal):
  # loop through nodes in LL if the value is less than partitionVal
  # add the node to a left list, if greater or equal add to right list
  # at the end the tail of the right list points to None and the tail
  # of the left list points to the head of the right list
  currentLeft = LinkedList()
  currentRight = LinkedList()
  currentNode = head
  if(head == None):
    return None
  else:
    while(currentNode != None):
      if(currentNode.value < partitionVal):
        currentLeft.addNode(currentNode)
      else:
        currentRight.addNode(currentNode)
      currentNode = currentNode.nextNode
  currentRight.tail.nextNode = None
  currentLeft.tail.nextNode = currentRight.head
  return currentLeft.head

testLL = LinkedList()
testLL.addNode(Node(3))
testLL.addNode(Node(5))
testLL.addNode(Node(8))
testLL.addNode(Node(5))
testLL.addNode(Node(10))
testLL.addNode(Node(2))
testLL.addNode(Node(1))

testOutput = partitionLL(testLL.head, 8)
currentNode = testOutput
while(currentNode != None):
  print(currentNode.value)
  currentNode = currentNode.nextNode