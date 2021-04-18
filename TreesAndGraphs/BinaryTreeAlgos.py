# Binary Tree Node class
# Each node in a Binary Tree has a left and right node
class TreeNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

  # Add a child to the next available spot on the node
  # if the node already has two children, return false
  def addChild(self, childNode):
    if(self.left == None):
      self.left = childNode
    elif(self.right == None):
      self.right = childNode
    else:
      return False
  
  # Set the value of the Node
  def setValue(self, value):
    self.value = value

# Binary Search Tree that inherits from the regular Binary Tree class
# A Binary Search Tree is a tree such that each value to the left of
# a root node of a subtree is less than/equal to the root. 
# Each value on the rightbof a subtree is greater than the root
class SearchTreeNode(TreeNode):

  # Add a child Node, call the addChildToTree helper function
  def addChild(self, nodeValue):
    self.addChildToTree(nodeValue, self)

  # This function will add a node into a Binary Search Tree
  # It will recursively call until the right position is found
  def addChildToTree(self, value, node):

    # Set the node's left node to a new SearchTreeNode
    # if the left node is empty and the value to insert
    # is less than or equal to the node's value
    if(value <= node.value and node.left == None):
      node.left = SearchTreeNode(value)

    # Set the node's right node to a new SearchTreeNode
    # if the right node is empty and the value to insert
    # is greater than the node's value
    elif(value > node.value and node.right == None):
      node.right = SearchTreeNode(value)

    # If the value to insert is less than or equal to the current node
    # and the node's left node is not empty, we must traverse
    # to the left of the tree to find the position to insert
    elif(value <= node.value and node.left != None):
      self.addChildToTree(value, node.left)

    # If the value to insert is greater than the current node
    # and the node's right node is not empty, we must traverse
    # to the right on the tree to find the position to insert
    elif(value > node.value and node.right != None):
      self.addChildToTree(value, node.right)
    else:
      return False

# In Order - Left, Root, Right
# In a BST, it will print the the nodes in numerical order
def inOrderTraversal(treeNode):

  # If the current node is empty return back to the function
  if(treeNode == None):
    return None
  
  # Traverse all the left nodes first
  inOrderTraversal(treeNode.left)

  # If all left nodes of a subtree are traversed, print the root
  print(treeNode.value)

  # Once the root of a subtree is traversed, traverse the right nodes
  inOrderTraversal(treeNode.right)

# Pre Order - Root, Left, Right (root is always first visited)
def preOrderTraversal(treeNode):

  # If the current node is empty return back to the function
  if(treeNode == None):
    return None

  # Visit and print the root of the subtree first
  print(treeNode.value)

  # Once the root has been visited, traverse the left subtree
  preOrderTraversal(treeNode.left)

  # Once the root and left subtree have been visited, traverse the right subtree
  preOrderTraversal(treeNode.right)

# Post Order - Left, Right, Root (root is always last visited)
def postOrderTraversal(treeNode):

  # If the current node is empty return back to the function
  if(treeNode == None):
    return None

  # Traverse the left subtree first
  postOrderTraversal(treeNode.left)

  # Once all left nodes visited in subtree, traverse right subtree
  postOrderTraversal(treeNode.right)

  # Once all left and right nodes of a subtree have been visited, visit the root
  print(treeNode.value)

#       8
#     /   \
#    4      9
#  /  \       \ 
# 2    5      10
# |
# 1
# In Order Traversal: 1, 2, 4, 5, 8, 9, 10
# Pre Order Traversal: 8, 4, 2, 1, 5, 9, 10
# Post Order Traversal: 1, 2, 5, 4, 10, 9, 8
