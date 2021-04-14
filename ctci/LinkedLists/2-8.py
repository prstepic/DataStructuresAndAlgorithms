class Node:
  def __init__(self, value=0, nextNode=None):
    self.value = value
    self.nextNode = nextNode
  
  def setValue(self, value):
    self.value = value

  def setNextNode(self, nextNode):
    self.nextNode = nextNode

# hash map solution, O(n) runtime, O(n) space
# where n is the length of the linked list
def hmFindLoop(headNode):
  if(headNode == None):
    return False
  nodesInList = set()
  while(headNode != None):
    if(id(headNode) in nodesInList):
      return headNode
    else:
      nodesInList.add(id(headNode))
      headNode = headNode.nextNode
  return False

# runner method, O(n-1) = O(n)
def runnerFindLoop(headNode):
  if(headNode == None):
    return False
  runnerOne = headNode
  runnerTwo = headNode
  while(runnerOne != None and runnerTwo != None):
    runnerOne = runnerOne.nextNode
    if(runnerTwo.nextNode != None):
        runnerTwo = runnerTwo.nextNode.nextNode
    else:
        return False

    if(runnerOne == runnerTwo and runnerOne):
      break
      
  if(runnerOne == None or runnerTwo == None):
    return False

  runnerOne = headNode
  while(runnerOne != runnerTwo):
    runnerOne = runnerOne.nextNode
    runnerTwo = runnerTwo.nextNode

  return runnerOne

