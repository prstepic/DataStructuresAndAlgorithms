class Stack:
  def __init__(self):
    self.stack = []

  def pop(self):
    if(len(self.stack) == 0):
      return False
    else:
      return self.stack.pop()
  
  def push(self, value):
    self.stack.append(value)
    
  def getSize(self):
    return len(self.stack)
  
  def peek(self):
    if(len(self.stack) == 0):
      return False
    return self.stack[len(self.stack) - 1]

class MyQueue:
  def __init__(self):
    self.stackOne = Stack()
    self.stackTwo = Stack()
  
  def add(self, value):
    if(self.stackOne.getSize() == 0):
      self.stackOne.push(value)
    else:
      while(self.stackOne.getSize() != 0):
        self.stackTwo.push(self.stackOne.pop())
      self.stackOne.push(value)
      while(self.stackTwo.getSize() != 0):
        self.stackOne.push(self.stackTwo.pop())

  def remove(self):
    if(self.stackOne.getSize() == 0):
      return False
    return self.stackOne.pop()

  def peek(self):
    if(self.stackOne.getSize() == 0):
      return False
    return self.stackOne.stack[self.stackOne.getSize() -1]

  def isEmpty(self):
    if(self.stackOne.getSize() == 0):
      return True
    else:
      return False