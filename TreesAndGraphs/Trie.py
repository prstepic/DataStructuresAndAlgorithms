# Class to represent a node in a Trie tree
# The node will have a list of children nodes and a character value
class TrieNode:
  def __init__(self, value=''):
    self.value = value
    self.children = []

  # Add a new node to the current node's list of children
  def addChild(self, valueToAdd):
    self.children.append(TrieNode(valueToAdd))
  
  # Determine if the node has a child node that stores a certain character
  # If so, return the index of this child node so it can be accessed
  def isChild(self, nodeToFind):
    for child in self.children:
      if(child.value == nodeToFind):
        return self.children.index(child)
    else:
      return -1
  
# Class to represent a Trie Tree. A Trie Tree is a directed tree (and therefore a graph)
# with nodes that contain characters. The Trie Tree contains valid words in a set
# Each word is represented by a branch in the tree that ends at a node with a value of *
# Each word must terminate with a * so prefixes in the tree are not counted as valid words
# The Trie Tree has one root node that has a null value. All nodes stem from this root.
class Trie:
  def __init__(self):
    self.root = TrieNode(None)
  
  # Function to add a string to the Trie tree, the word string will be added character by character
  # O(n) runtime as each character in the string will be iterated
  def addString(self, stringToAdd):

    # Start at the root of the Trie Tree before evaluating the string to add
    currentNode = self.root

    # Iterate through the string, at each character evaluate if it is already a child of the current node
    # If it is then traverse to that node. This is so we can build the new string from existing prefixes
    # If the character is not in the children. Allocate a new node and add it to the current node's children
    # Then traverse to that child node. All remaining characters will stem from this child node
    for character in stringToAdd:
      index = currentNode.isChild(character)
      if(index != -1):
        currentNode = currentNode.children[index]
      else:
        currentNode.addChild(character)
        currentNode = currentNode.children[len(currentNode.children) -1]

    # Add an ending flag node to the end of the branch representing the string, marking the end of the word
    currentNode.addChild('*')
      
  # This function returns all possible words with an inputted prefix
  def findWordsWithPrefix(self, prefix):

    # Starting at the root, traverse the Trie tree until the prefix is fully traversed in the graph
    # possible words will be found starting at this point
    currentNode = self.root
    count = 0
    for letter in prefix:
      index = currentNode.isChild(letter)
      if(index != -1):
        currentNode = currentNode.children[index]
        count += 1

    # if the prefix was not found in the tree or only partially found, return False
    if(count == 0 or count != len(prefix)):
      return False

    # Use the prefixDFS helper function to build a list of words in the tree with the given prefix
    else:
      returnList = []
      self.__prefixDFS(currentNode, prefix, returnList)
      return returnList
  
  # Helper function for findWordsWithPrefix, functions like a depth first traversal of the tree
  def __prefixDFS(self, node, word, listOfWords):

    # Once the end of the branch is reached, add the word to the list of words
    if(node.value == '*'):
      listOfWords.append(word)
      return
      
    else:
      # Starting at the inputted node, recurse and build a word from the rest of the children
      for child in node.children:
        temp = word
        if(child.value != '*'):
          word = word + child.value
        self.__prefixDFS(child, word, listOfWords)

        # reset word to what it was before the recursion
        word = temp

