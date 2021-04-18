# Class to represent a Min Heap
# The minimum element of the set is the top of the heap
# Each subtree in the heap also holds that its root is the minimum
class MinHeap:

  # Store the heap in an array
  def __init__(self):
    self.heap = []

  # Sets the minimum of the heap when a new value is entered
  def setMinInsert(self, index):

    # If the value at index of the heap is less than its parent
    # keep it where it is and return
    if(self.heap[int((index - 1) / 2)] <= self.heap[index]):
      return True
    
    # Else swap the value at index in the heap with its parent
    # then recurse at the parent index to check the rest of the heap
    else:
      temp = self.heap[index]
      self.heap[index] = self.heap[int((index - 1) / 2)]
      self.heap[int((index - 1) / 2)] = temp
      self.setMinInsert(int((index - 1) / 2))

  # Sets the minimum of the heap when the minimum is extraced
  def setMinExtract(self, index):

    indexToSwap = 0

    # If the left child is out of range of the heap
    # return to the function
    if((2*index) + 1 >= len(self.heap)):
      return False
    else:

      # If the right child of at the value's index is empty
      # set the index of insert to the value's left child
      if((2*index) + 2 >= len(self.heap)):
        indexToSwap = (2*index) + 1

      # If the left and right children are not empty
      # find the least of the two children. This will be the
      # index that will be switched with the value inputted into the function
      elif(self.heap[(2*index) + 1] <= self.heap[(2*index) + 2]):
        indexToSwap = (2*index) + 1
      else:
        indexToSwap = (2*index) + 2
      
      # Swap the value inserted into the function with the
      # calculated index to swap (either left or right child)
      temp = self.heap[index]
      self.heap[index] = self.heap[indexToSwap]
      self.heap[indexToSwap] = temp

      # recursively check the children values after the swap
      # to maintain 
      self.setMinExtract(indexToSwap)
    
  # Inserts a new value into the heap, new values are entred at the 
  # last position in the heap, then the heap will be reordered to 
  # maintain that the top element of a subtree is the minimum
  def insert(self, value):
    self.heap.append(value)
    if(len(self.heap) > 1):
      self.setMinInsert(len(self.heap) - 1)
  
  # Removes the minimum of the heap, the minimum is stored at the top
  # or first position of the heap. The last value in the heap becomes the 
  # new top of the heap. Then the heap is reordered in order to keep the
  # minimum on top
  def extractMin(self):
    if(len(self.heap) == 0):
      return False
    currentMin = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.setMinExtract(0)
    return currentMin

