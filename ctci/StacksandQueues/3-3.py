class Stack:
  def __init__(self, stackSize):
    self.stackSize = stackSize
    self.stack = []

  def pop(self):
    if(len(self.stack) == 0):
      return False
    else:
      self.stackSize -= 1
      return self.stack.pop()
  
  def push(self, value):
    if(len(self.stack) == self.stackSize):
      return False
    else:
      self.stack.append(value)
      self.stackSize += 1
    
  def getSize(self):
    return len(self.stack)

class SetOfStacks:
  def __init__(self, stackThreshold):
    self.currentStack = 0
    self.stackThreshold = stackThreshold
    self.listOfStacks = []
    self.listOfStacks.append(Stack(stackThreshold))

  def pop(self):
    if(self.listOfStacks[self.currentStack].getSize() == 0):
      if(self.currentStack == 0):
        return False
      else:
        self.currentStack -= 1
        self.listOfStacks = self.listOfStacks[:-1]
    poppedVal = self.listOfStacks[self.currentStack].pop()
    if(self.listOfStacks[self.currentStack].getSize() == 0):
      self.listOfStacks = self.listOfStacks[:-1]
      self.currentStack -= 1
    if(self.currentStack == -1):
      self.listOfStacks.append(Stack(self.stackThreshold))
      self.currentStack = 0
    return poppedVal

  def push(self, value):
    if(self.listOfStacks[self.currentStack].getSize() == self.stackThreshold):
      self.listOfStacks.append(Stack(self.stackThreshold))
      self.currentStack += 1
    self.listOfStacks[self.currentStack].push(value)

  def popAt(self, indexOfStack):
    if(indexOfStack < 0 or indexOfStack > len(self.listOfStacks)):
      return False
    else:
      if(self.listOfStacks[indexOfStack].getSize() == 0):
        return False
      poppedVal = self.listOfStacks[indexOfStack].pop()
      if(self.listOfStacks[indexOfStack].getSize() == 0):
        if(indexOfStack == len(self.listOfStacks) - 1):
          self.currentStack -= 1
        self.listOfStacks = self.listOfStacks[0:indexOfStack] + self.listOfStacks[indexOfStack:]
      return poppedVal