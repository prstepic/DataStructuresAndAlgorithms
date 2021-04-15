class MinStack:
  def __init__(self):
    self.stack = []

  def pop(self):
    if(len(self.stack) == 0):
      return False
    return self.stack.pop()
  
  def push(self, value):
    if(len(self.stack) == 0):
      self.stack.append(value)
      return
    tempStack = []
    while(self.stack[len(self.stack) - 1] <= value):
      tempStack.append(self.stack.pop())
      if(len(self.stack) == 0):
        break
    self.stack.append(value)
    while(len(tempStack) != 0):
      self.stack.append(tempStack.pop())
  
  def peek(self):
    if(len(self.stack) == 0):
      return False
    return self.stack[len(self.stack) - 1]
  
  def isEmpty(self):
    if(len(self.stack) == 0):
      return True
    else:
      return False