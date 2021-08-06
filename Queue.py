class Queue:
    def __init__(self) -> None:
        self.queueList = []
        
    def dequeue(self):
        if(self.queueList):
            return self.queueList.pop(0)
        else:
            return None

    def enqueue(self, val) -> None:
        self.queueList.append(val)

    def first(self):
        if(self.queueList):
            return self.queueList[0]
        else:
            return None
            
    def size(self) -> int:
        return len(self.queueList)