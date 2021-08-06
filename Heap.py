class MinHeap:
    def __init__(self) -> None:
        self.heapList = []
    
    def heappush(self, val) -> None:
        self.heapList.append(val)
        self.__heapifyPush(self.size() - 1)

    def heappop(self):
        if(self.heapList):
            temp = self.heaptop()
            self.__swap(0, -1)
            self.heapList.pop()
            self.__heapifyPop(0)
            return temp
        else:
            return None

    def heaptop(self):
        if(self.heapList):
            return self.heapList[0]
        else:
            return None
        
    def size(self) -> int:
        return len(self.heapList)

    def __heapifyPush(self, index) -> None:
        parentIndex = int(index / 2)
        if(index == 0):
            return
        if(self.heapList[parentIndex] > self.heapList[index]):
            self.__swap(parentIndex, index)
            self.__heapifyPush(parentIndex)
        else:
            return
    
    def __heapifyPop(self, index):
        childIndexLeft = (index * 2) + 1
        childIndexRight = (index * 2) + 2
        smallestChild = childIndexLeft
        if(childIndexLeft >= self.size()):
            return
        elif(childIndexRight < self.size()):
            if(self.heapList[childIndexRight] < self.heapList[childIndexLeft]):
                smallestChild = childIndexRight
        if(self.heapList[index] > self.heapList[smallestChild]):
            self.__swap(index, smallestChild)
            self.__heapifyPop(smallestChild)
        else:
            return

    def __swap(self, indexOne, indexTwo) -> None:
        if(len(self.heapList) > 1):
            temp = self.heapList[indexOne]
            self.heapList[indexOne] = self.heapList[indexTwo]
            self.heapList[indexTwo] = temp

class MaxHeap:
    def __init__(self) -> None:
        self.heapList = []
    
    def heappush(self, val) -> None:
        self.heapList.append(val)
        self.__heapifyPush(self.size() - 1)

    def heappop(self):
        if(self.heapList):
            temp = self.heaptop()
            self.__swap(0, -1)
            self.heapList.pop()
            self.__heapifyPop(0)
            return temp
        else:
            return None

    def heaptop(self):
        if(self.heapList):
            return self.heapList[0]
        else:
            return None
        
    def size(self) -> int:
        return len(self.heapList)

    def __heapifyPush(self, index) -> None:
        parentIndex = int(index / 2)
        if(index == 0):
            return
        if(self.heapList[parentIndex] < self.heapList[index]):
            self.__swap(parentIndex, index)
            self.__heapifyPush(parentIndex)
        else:
            return
    
    def __heapifyPop(self, index):
        childIndexLeft = (index * 2) + 1
        childIndexRight = (index * 2) + 2
        greatestChild = childIndexLeft
        if(childIndexLeft >= self.size()):
            return
        elif(childIndexRight < self.size()):
            if(self.heapList[childIndexRight] > self.heapList[childIndexLeft]):
                greatestChild = childIndexRight

        if(self.heapList[index] < self.heapList[greatestChild]):
            self.__swap(index, greatestChild)
            self.__heapifyPop(greatestChild)
        else:
            return

    def __swap(self, indexOne, indexTwo) -> None:
        if(len(self.heapList) > 1):
            temp = self.heapList[indexOne]
            self.heapList[indexOne] = self.heapList[indexTwo]
            self.heapList[indexTwo] = temp
