# Binary Tree Node class
class TreeNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

  def addChild(self, childNode):
    if(self.left == None):
      self.left = childNode
    elif(self.right == None):
      self.right = childNode
    else:
      return False
  
  def setValue(self, value):
    self.value = value

class SearchTreeNode(TreeNode):
  def addChild(self, nodeValue):
    addChildToTree(nodeValue, self)

def addChildToTree(value, node):
  if(value <= node.value and node.left == None):
    node.left = SearchTreeNode(value)
  elif(value > node.value and node.right == None):
    node.right = SearchTreeNode(value)
  elif(value <= node.value and node.left != None):
    addChildToTree(value, node.left)
  elif(value > node.value and node.right != None):
    addChildToTree(value, node.right)
  else:
    return False

# In Order - Left, Root, Right
def inOrderTraversal(treeNode):
  if(treeNode == None):
    return None
  inOrderTraversal(treeNode.left)
  print(treeNode.value)
  inOrderTraversal(treeNode.right)

# Pre Order - Root, Left, Right (root is always first visited)
def preOrderTraversal(treeNode):
  if(treeNode == None):
    return None
  print(treeNode.value)
  preOrderTraversal(treeNode.left)
  preOrderTraversal(treeNode.right)

# Post Order - Left, Right, Root (root is always last visited)
def postOrderTraversal(treeNode):
  if(treeNode == None):
    return None
  postOrderTraversal(treeNode.left)
  postOrderTraversal(treeNode.right)
  print(treeNode.value)

