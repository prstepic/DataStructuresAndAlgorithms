class MinHeap:
  def __init__(self):
    self.heap = []

  def setMinInsert(self, index):
    if(self.heap[int((index - 1) / 2)] <= self.heap[index]):
      return True
    else:
      temp = self.heap[index]
      self.heap[index] = self.heap[int((index - 1) / 2)]
      self.heap[int((index - 1) / 2)] = temp
      self.setMinInsert(int((index - 1) / 2))

  def setMinExtract(self, index):
    indexToSwap = 0
    if((2*index) + 1 >= len(self.heap)):
      return True
    else:
      if((2*index) + 2 >= len(self.heap)):
        indexToSwap = (2*index) + 1
      elif(self.heap[(2*index) + 1] <= self.heap[(2*index) + 2]):
        indexToSwap = (2*index) + 1
      else:
        indexToSwap = (2*index) + 2
      temp = self.heap[index]
      self.heap[index] = self.heap[indexToSwap]
      self.heap[indexToSwap] = temp
      self.setMinExtract(indexToSwap)
    
  def insert(self, value):
    self.heap.append(value)
    if(len(self.heap) > 1):
      self.setMinInsert(len(self.heap) - 1)
  
  def extractMin(self):
    if(len(self.heap) == 0):
      return False
    currentMin = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.setMinExtract(0)
    return currentMin

