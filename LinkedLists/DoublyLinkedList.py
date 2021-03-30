# Node class that will represent an object in a Linked List
class Node:

    # Each node has an internal value, a next Node, and a previous Node (defaults are None)
    def __init__(self, value=0, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

    # Set/Change the internal value of the Node
    def setValue(self, newValue):
        self.value = newValue

    # Set/Change the pointed next Node
    def setNextNode(self, newNode):
        self.nextNode = newNode

    # Set/Change the pointed previous Node
    def setPrevNode(self, prevNode):
        self.prevNode = prevNode

# Class that will represent a Linked List where each Node points in both directions
# Additionally, the list has a first Node and last Node attribute
class DoublyLinkedList:

    # Initialize the list with a head (first element) and tail (last element)
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        if(head == None and tail != None):
            self.head = tail
        elif(head != None and tail == None):
            self.tail = head

    # Inserts a Node at the end of the list with an internal value (Naive solution)
    # If the list is empty, this Node becomes the head and tail of the list
    # Else traverse the list until the end is reached, then insert the Node 
    # Point the previous tail to the new Node and the new Node points back at the previous tail
    # The new Node becomes the tail
    def insertNewNode(self, valueToInsert):
        newNode = Node(valueToInsert)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            currentNode = self.head
            while(currentNode.nextNode != None):
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode
            newNode.prevNode = currentNode
            self.tail = newNode

    # Traverse the list forward, visit each node until the end is reached, starting at the head
    # If the list is empty (head is empty), print an empty list
    def traverseForward(self):
        currentNode = self.head
        if(self.head == None):
            print("[]")
        while(currentNode != None):
            print(currentNode.value)
            currentNode = currentNode.nextNode

    # Traverse the list backwards, vist each node until the end is reached, starting at the tail
    # If the list is empty (tail is empty), print an empty list     
    def traverseBackward(self):
        currentNode = self.tail
        if(self.tail == None):
            print("[]")
        while(currentNode != None):
            print(currentNode.value)
            currentNode = currentNode.prevNode
    
    # Faster version of the insert at end function (O(1))
    # Since the tail is stored within a Doubly Linked List object, we can directly insert
    # An element at the end of the tail without traversing the list
    # If the list is empty (tail is empty), set the head and tail of the list to the new Node
    # Else point the current tail to the new Node, new Node points backwards to current tail
    # The new Node then becomes the new tail
    def insertNewNodeFast(self, valueToInsert):
        newNode = Node(valueToInsert)
        if(self.tail == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNextNode(newNode)
            newNode.setPrevNode(self.tail)
            self.tail = newNode
    
    # Search for a Node in the list with a certain internal value
    # If the list is empty(head is empty), return -1
    # Else traverse the list forward until the internal value is found, print the index
    # If all Nodes are visited and the Node is not found, return -1
    def searchForValue(self, valueToFind):
        if(self.head == None):
            print("LIST IS EMPTY")
            return -1
        currentNode = self.head
        index = 0
        while(currentNode != None):
            if(currentNode.value == valueToFind):
                return index
            else:
                currentNode = currentNode.nextNode
            index += 1
        print("VALUE NOT FOUND")
        return -1

    # Insert a Node at a certain position in the list, position must be greater than 0
    # If the position is 0 (beginning of the list), and the list is empty, the new Node 
    # becomes the head and tail. Else the current head points backwards to the new Node.
    # The new Node points forward to the current head, and becomes the new head
    # If the position is not 0, traverse the list until the inputted position is reached
    # If the current Node at the index is not the tail, point the current Node forward
    # to the new Node, new Node points backward to the current Node, the new Node
    # points forward to the current Node's next Node, and the current Node's next Node's 
    # previous Node points backwards to the new Node. If the current Node is the tail
    # then do the same steps but instead of pointing the current Node's next Node's previous
    # Node (in this case would be None) to the new Node, set the new Node as the tail
    # the new Node will now point forwards to None. (None has no prevNode attribute)
    def insertAtPosition(self, valueToInsert, positionToInsert):
        if(positionToInsert < 0):
            print("INDEX OUT OF BOUNDS")
            return -1
        newNode = Node(valueToInsert)
        if(positionToInsert == 0):
            if(self.head == None):
                self.head = newNode
                self.tail = newNode
            else:
                self.head.prevNode = newNode
                newNode.nextNode = self.head
                self.head = newNode
        else:
            index = 0
            currentNode = self.head
            while(index < positionToInsert):
                if(currentNode == None):
                    print("INDEX OUT OF BOUNDS")
                    return -1
                else:
                    if(index == positionToInsert - 1):
                        if(currentNode.nextNode != None):
                            currentNode.nextNode.prevNode = newNode
                        else:
                            self.tail = newNode
                        newNode.nextNode = currentNode.nextNode
                        currentNode.nextNode = newNode
                        newNode.prevNode = currentNode
                    else:
                        currentNode = currentNode.nextNode
                index += 1


doublyLL = DoublyLinkedList()

# 10
doublyLL.insertAtPosition(10, 0)

# 20, 10
doublyLL.insertAtPosition(20, 0)

# 20, 10, 30
doublyLL.insertAtPosition(30, 2)

# 20, 10, 30, 40
doublyLL.insertNewNode(40)

# 20, 10, 30, 40, 50
doublyLL.insertNewNodeFast(50)

# 20, 10, 30, 40, 50, 60
doublyLL.insertAtPosition(60, 5)

# Should print 20, 10, 30, 40, 50, 60
print("Traverse in forward order:")
doublyLL.traverseForward()

# Should print 60, 50, 40, 30, 10, 20
print("Traverse in reverse order:")
doublyLL.traverseBackward()

# Should print 20
print("Head:")
print(doublyLL.head.value)

# Should print 60
print("Tail:")
print(doublyLL.tail.value)

# Should print 0
print("index of 20:")
print(doublyLL.searchForValue(20))

# Should print 1
print("index of 10:")
print(doublyLL.searchForValue(10))

# Should print 2
print("index of 30:")
print(doublyLL.searchForValue(30))

# Should print 3
print("index of 40:")
print(doublyLL.searchForValue(40))

# Should print 4
print("index of 50:")
print(doublyLL.searchForValue(50))

# Should print 5
print("index of 60:")
print(doublyLL.searchForValue(60))

# Should print "VALUE NOT FOUND \n -1"
print("index of 200:")
print(doublyLL.searchForValue(200))