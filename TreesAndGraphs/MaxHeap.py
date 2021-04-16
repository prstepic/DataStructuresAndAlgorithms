class MaxHeap:
  def __init__(self):
    self.heap = []

  def setMaxInsert(self, index):
    if(self.heap[int((index - 1) / 2)] >= self.heap[index]):
      return True
    else:
      temp = self.heap[index]
      self.heap[index] = self.heap[int((index - 1) / 2)]
      self.heap[int((index - 1) / 2)] = temp
      self.setMaxInsert(int((index - 1) / 2))

  def setMaxExtract(self, index):
    indexToSwap = 0
    if((2*index) + 1 >= len(self.heap)):
      return True
    else:
      if((2*index) + 2 >= len(self.heap)):
        indexToSwap = (2*index) + 1
      elif(self.heap[(2*index) + 1] >= self.heap[(2*index) + 2]):
        indexToSwap = (2*index) + 1
      else:
        indexToSwap = (2*index) + 2
      temp = self.heap[index]
      self.heap[index] = self.heap[indexToSwap]
      self.heap[indexToSwap] = temp
      self.setMaxExtract(indexToSwap)
    
  def insert(self, value):
    self.heap.append(value)
    if(len(self.heap) > 1):
      self.setMaxInsert(len(self.heap) - 1)
  
  def extractMax(self):
    if(len(self.heap) == 0):
      return False
    currentMax = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.setMaxExtract(0)
    return currentMax