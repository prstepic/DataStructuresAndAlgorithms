class Node:
  def __init__(self, value='a', nextNode=None):
    self.value = value
    self.nextNode = nextNode
  
  def setValue(self, value):
    self.value = value

  def setNextNode(self, nextNode):
    self.nextNode = nextNode

def isPalindrome(head):
  if(head == None):
    return False
  stack = []
  stack.append(head.value)
  listLength = 0
  currentNode = head
  while(currentNode != None):
    listLength += 1
    currentNode = currentNode.nextNode
  if(listLength == 1):
    return True
  
  head = head.nextNode
  index = 1
  if(listLength % 2 == 0):
    while(head != None):
      if(head.value == stack[len(stack) - 1] and index >= listLength/2):
        stack.pop()
      else:
        stack.append(head.value)
      head = head.nextNode
      index += 1
  else:
    while(head != None):
      if(head.value == stack[len(stack) - 1] and index > int(listLength/2)):
        stack.pop()
      elif(index != int(listLength / 2)):
        stack.append(head.value)
      head = head.nextNode
      index += 1

  if(len(stack) == 0):
    return True
  else:
    return False


node1 = Node('a')
node2 = Node('a')
node3 = Node('c')
node4 = Node('a')
node5 = Node('b')
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
print(isPalindrome(node1))