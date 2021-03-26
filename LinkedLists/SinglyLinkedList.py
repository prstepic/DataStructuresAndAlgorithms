# Node class that will represent a Node in the Linked List
class Node:

    # Initialize a Node to a int value (0 is default) and a nextNode (None is default)
    def __init__(self, value=0, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    # Set / Change Value stored within the Node
    def setValue(self, newValue):
        self.value = newValue

    # Set / Change the next Node that this Node points to
    def setNextNode(self, newNode):
        self.nextNode = newNode

# Singly Linked List class that represents a list where each Node only points to its next Node
class SinglyLinkedList:

    # Initialize the list with a head (first Node in the list, None by default)
    def __init__(self, head = None):
        self.head = head
    
    # Print each Node in the list. Visit each Node in the list by jumping to a Node's next Node
    def traverseList(self):
        currentNode = self.head
        while(currentNode != None):
            print(currentNode.value)
            currentNode = currentNode.nextNode

    # Insert a new Node at the end of the list. Create a Node with the inputted value
    # If the list is empty (head = None), insert the Node at the beginning of the list
    # Else traverse the list until the end is reached (the next Node is None) and insert the Node
    def insertNewNode(self, valueToInsert):
        newNode = Node(valueToInsert)
        if(self.head == None):
            self.head = newNode
        else:
            currentNode = self.head
            while(currentNode.nextNode != None):
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode

    # Insert a new Node at a certain position in the list (indexing starts at 0)
    # This function will put the new Node at the position, positionToInsert, in the new list
    # If positionToInsert is 0, the new Node becomes the head of the list
    # Else traverse the list until the desired position is reached, insert the Node and point it
    # to the previous Node's next Node. The previous Node now points to the new Node
    def insertAtPosition(self, valueToInsert, positionToInsert):
        newNode = Node(valueToInsert)
        if(positionToInsert < 0):
            print("INDEX OUT OF BOUNDS OF LIST")
            return -1
        if(positionToInsert == 0):
            newNode.nextNode = self.head
            self.head = newNode
        else:
            currentNode = self.head
            index = 0
            while(index < positionToInsert):
                if(currentNode == None):
                    print("INDEX OUT OF BOUNDS OF LIST")
                    return -1
                else:
                    if index == positionToInsert - 1:
                        newNode.nextNode = currentNode.nextNode
                        currentNode.nextNode = newNode
                    else:
                        currentNode = currentNode.nextNode
                index += 1

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
                

    

singlyLL = SinglyLinkedList()
singlyLL.insertNewNode(7)
singlyLL.insertNewNode(6)
singlyLL.insertNewNode(9)
singlyLL.insertNewNode(11)

# Should print 7, 6, 9, 11
print("Order 1:")
singlyLL.traverseList()

# 7, 6, 10, 9, 11
singlyLL.insertAtPosition(10, 2)

# 7, 6, 10, 88, 9, 11
singlyLL.insertAtPosition(88, 3)

# 90, 7, 6, 10, 88, 9, 11
singlyLL.insertAtPosition(90, 0)

# 90, 7, 6, 10, 88, 9, 11, 100
singlyLL.insertAtPosition(100, 7)

# Should print 90, 7, 6, 10, 88, 9, 11, 100
print("Order 2:")
singlyLL.traverseList()

print(singlyLL.searchForValue(8))
print(singlyLL.searchForValue(7))
print(singlyLL.searchForValue(100))


