class TreeNode:
    def __init__(self, value=None) -> None:
        self.val = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, root=None) -> None:
        self.root = None
    
    def addNode(self, value) -> None:
        if(self.root == None):
            self.root = TreeNode(value)
            return 
        currNode = self.root
        bfsQueue = []
        bfsQueue.append(self.root)
        while(bfsQueue):
            currNode = bfsQueue.pop(0)
            if(currNode.left != None):
                bfsQueue.append(currNode.left)
            if(currNode.right != None):
                bfsQueue.append(currNode.right)
        if(currNode.left == None):
            currNode.left = TreeNode(value)
        else:
            currNode.right == TreeNode(value)

    def inorder(self) -> None:
        self.__inorderRecurse(self.root)

    def __inorderRecurse(self, node: TreeNode) -> None:
        if(node == None):
            return
        self.__inorderRecurse(node.left)
        print(node.val)
        self.__inorderRecurse(node.right)
    
    def preorder(self) -> None:
        self.__preorderRecurse(self.root)

    def __preorderRecurse(self, node: TreeNode) -> None:
        if(node == None):
            return
        print(node.val)
        self.__preorderRecurse(node.left)
        self.__preorderRecurse(node.right)

    def postorder(self) -> None:
        self.__postorderRecurse(self.root)
    
    def __postorderRecurse(self, node: TreeNode) -> None:
        if(node == None):
            return
        self.__postorderRecurse(node.left)
        self.__postorderRecurse(node.right)
        print(node.val)
    
class BinarySearchTree(Tree):
    def addNode(self, value) -> None:
        if(self.root):
            self.__findIndexForNew(self, value, self.root)
        else:
            self.root = TreeNode(value)
    
    def __findIndexForNew(self, valToInsert: int, nodeToCompare: TreeNode) -> TreeNode:
        if(nodeToCompare == None):
            return TreeNode(valToInsert)
        elif(valToInsert <= nodeToCompare.val):
            nodeToCompare.left = self.__findIndexForNew(valToInsert, nodeToCompare.left)
        else:
            nodeToCompare.right = self.__findIndexForNew(valToInsert, nodeToCompare.right)
        return nodeToCompare

    def search(self, value) -> bool:
        return self.__searchRecurse(self.root, value)

    def __searchRecurse(self, node, valToFind) -> bool:
        if(node == None):
            return False
        elif(node.val == valToFind):
            return True
        elif(node.val < node.val):
            return self.__searchRecurse(node.left)
        else:
            return self.__searchRecurse(node.right)
        
    def maxInTree(self):
        return self.__findMaxRecurse(self.root)
    
    def __findMaxRecurse(self, node):
        if(node == None):
            return -1 * float('inf')
        return max(node, self.__findMaxRecurse(node.right))

    def minInTree(self):
        return self.__findMinRecurse(self.root)

    def __findMinRecurse(self, node):
        if(node == None):
            return float('inf')
        return min(node.val, self.__findMinRecurse(node.left))
    