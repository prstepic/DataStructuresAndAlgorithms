# Node class that will represent an object in a Linked List
class Node:

    # Each node has an internal value, a next Node, and a previous Node (defaults are None)
    def __init__(self, value=0, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    # Set/Change the internal value of the Node
    def setValue(self, value):
        self.value = value

    # Set/Change the pointed next Node
    def setNextNode(self, nextNode):
        self.nextNode = nextNode

# Class that will represent a Circled Linked List
# Each node points forward to its next Node and the tail Node points back to the head
class CircledLinkedList:

    # Initialize the Circled Linked List with a head and tail Node (None by default)
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    # Traverse and print the Circled Linked List exactly once, ending at the tail Node
    # Print an empty list if the head is None (Linked List is empty)
    def traverseList(self):
        if(self.head == None):
            print("[]")
        else:
            print(self.head.value)
            currentNode = self.head.nextNode
            while(currentNode != self.head):
                print(currentNode.value)
                currentNode = currentNode.nextNode

    # Insert a new Node at the end of the Linked List, after the tail Node
    # If the head Node is None (Linked List is empty), set the head and tail to the new Node
    # Then point the head to the tail and tail to the head (meaning it will point to itself)
    # If the Linked List is not empty, insert the Node after the tail. Point the tail to the new Node
    # Point the new Node to the head Node. The new Node then becomes the tail of the Linked List
    def insertNewNode(self, valueToInsert):
        newNode = Node(valueToInsert)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
            self.head.nextNode = self.tail
            self.tail.nextNode = self.head
        else:
            self.tail.nextNode = newNode
            newNode.nextNode = self.head
            self.tail = newNode
    
    # Insert a new Node at a given position. If the desired position is 0 (front of the list)
    # and the Linked List is empty use the insertNewNode function to insert the new Node.
    # if there is only one element in the list, point the new Node to the head. The old head
    # (and tail) will point to the new Node. The new tail then becomes the old head.
    # The new head is now the new Node. Else if there is more than one element in the Linked List,
    # Point the new Node to the old head, the tail now points to the new Node, and the new Node becomes the head
    # If the desired position is not 0, traverse the list until the Node to insert after is reached or the end 
    # Of the list is reached (loops back to head). Once this desired Node is reached, Point the new Node to the
    # Desired Node's next Node, point the desired Node to the new Node, and if the desired Node is the tail
    # Make the new Node the new tail and it will now point to the head of the list
    def insertAtPosition(self, valueToInsert, positionToInsert):
        if(positionToInsert < 0):
            print("Index out of range")
            return -1
        else:
            newNode = Node(valueToInsert)
            if(positionToInsert == 0):
                if(self.head == None):
                    self.insertNewNode(valueToInsert)
                elif(self.head == self.tail):
                    newNode.nextNode = self.head
                    self.head.nextNode = newNode
                    self.tail = self.head
                    self.head = newNode
                else:
                    newNode.nextNode = self.head
                    self.tail.nextNode = newNode
                    self.head = newNode
            else:
                index = 0
                currentNode = self.head
                while(index < positionToInsert):
                    if(currentNode == self.head and index != 0):
                        print("index out of range")
                        return -1
                    else:
                        if(index == positionToInsert -1):
                            newNode.nextNode = currentNode.nextNode
                            currentNode.nextNode = newNode
                            if(currentNode == self.tail):
                                self.tail = newNode
                        else:
                            currentNode = currentNode.nextNode
                        index += 1

    # Find a desired value in a list. If the list is empty, return -1 as the element will not exist.
    # If the head contains the value to find, return 0. Else, starting with the head's next Node,
    # Look for the value to find until the head is reached again. If there is only one element in
    # the list, then the head's next node is once again the head so the while loop will not trigger,
    # And the value will not be found
    def searchForValue(self, valueToFind):
        if(self.head == None):
            print("Value not found")
            return -1
        elif(self.head.value == valueToFind):
            return 0
        else:
            currentNode = self.head.nextNode
            index = 1
            while(currentNode != self.head):
                if(currentNode.value == valueToFind):
                    return index
                else:
                    currentNode = currentNode.nextNode
                index += 1
            print("Value not found")
            return -1
    

circledLL = CircledLinkedList()
print("Print 1 (expected: [] Value Not Found -1)")
circledLL.traverseList()
print(circledLL.searchForValue(9))

circledLL.insertNewNode(5)
print("Print 2 (expected: 5 0)")
circledLL.traverseList()
print(circledLL.searchForValue(5))

circledLL.insertNewNode(6)
circledLL.insertNewNode(7)
print("Print 3 (expected 5 6 7 1)")
circledLL.traverseList()
print(circledLL.searchForValue(6))

print("Printing head value (expected 5)")
print(circledLL.head.value)
print("Printing tail value (expected 7)")
print(circledLL.tail.value)

print("Find 5 and 20 in list (Expected: 0 Value not found -1)")
print(circledLL.searchForValue(5))
print(circledLL.searchForValue(20))

print("----------------")
print("Testing insert at position")

newCLL = CircledLinkedList()
newCLL.insertAtPosition(10, 0)
newCLL.insertAtPosition(20, 0)
newCLL.insertAtPosition(30, 0)
newCLL.insertAtPosition(15, 1)
newCLL.insertAtPosition(19, 4)
newCLL.insertAtPosition(14, 2)
newCLL.insertAtPosition(16, 0)
print("Expected 16, 30, 15, 14, 20, 10, 19")
newCLL.traverseList()
print("----------------")
print(newCLL.head.value)
print(newCLL.tail.value)




