from typing import List
class TrieNode:
    def __init__(self, letter: str):
        self.val = letter
        self.children = {}
        self.endOfWord = False
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(None)
    
    def addWord(self, word: str) -> None:
        currNode = self.root
        for letter in word:
            if(letter in currNode.children):
                currNode = currNode.children[letter]
            else:
                newNode = TrieNode(letter)
                currNode.children[letter] = newNode
                currNode = newNode
        currNode.endOfWord = True

    def searchWord(self, word: str) -> bool:
        currNode = self.root
        for letter in word:
            if(letter not in currNode.children):
                return False
            currNode = currNode.children[letter]
        return currNode.endOfWord
    
    def wordsWithPrefix(self, prefix: str) -> List[str]:
        if(prefix[0] not in self.root.children):
            return []
        currNode = self.root
        for letter in prefix:
            if(letter not in prefix):
                return []
            currNode = currNode.children[letter]
        processStack = []
        processStack.append(currNode)
        returnList = []
        currWord = ""
        notFirst = False
        while(processStack):
            currNode = processStack.pop()
            for letter,child in currNode.children.items():
                processStack.append(child)
            if(notFirst):
                currWord += currNode.val
            else:
                notFirst = True
            if(currNode.endOfWord == True):
                returnList.append(prefix + currWord)
            if(len(currNode.children) == 0):
                currWord = ""
        return returnList