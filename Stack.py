class Stack:
    def __init__(self) -> None:
        self.stackList = []
        
    def pop(self):
        if(self.stackList):
            return self.stackList.pop()
        else:
            return None

    def push(self, val) -> None:
        self.stackList.append(val)

    def top(self):
        if(self.stackList):
            return self.stackList[-1]
        else:
            return None

    def size(self) -> int:
        return len(self.stackList)
    
