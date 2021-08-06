class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.root = None
    
    def addNode(self, value) -> None:
        if(value in self.nodes):
            return
        if(len(self.nodes) == 0):
            self.root = value
        self.nodes[value] = set()
    
    def BFS(self) -> None:
        if(not self.root):
            print("No Nodes in graph")
            return
        visited = set()
        self.__BFSHelper(self.root, visited)
        for node in self.nodes:
            if(node not in visited):
                self.__BFSHelper(node, visited)
            print('visited', visited)

    def __BFSHelper(self, node, visited: set) -> None:
        processQueue = [node]
        while processQueue:
            currNode = processQueue.pop(0)
            for child in self.nodes[currNode]:
                if(child not in visited):
                    processQueue.append(child)
                    visited.add(child)
            print(currNode)
            visited.add(currNode)  
    
    def dfsIter(self) -> None:
        if(not self.root):
            print('No nodes in graph')
            return
        processStack = [self.root]
        visited = set()
        while processStack:
            currNode = processStack.pop()
            for child in self.nodes[currNode]:
                if(child not in visited):
                    processStack.append(child)
                    visited.add(child)
            print(currNode)
            visited.add(currNode)

    def dfsRec(self) -> None:
        if(not self.root == None):
            print('No nodes in graph')
            return
        visited = set()
        self.__dfsRecHelper(self.root, visited)
        for node in self.nodes:
            if(node not in visited):
                self.__dfsRecHelper(node, visited)

    def __dfsRecHelper(self, node, visited: set) -> None:
        if(node in visited):
            return
        visited.add(node)
        print(node)
        for child in self.nodes[node]:
            if(child not in visited):
                self.__dfsRecHelper(child, visited)

class UndirectedGraph(Graph):
    def addEdge(self, nodeOne, nodeTwo) -> None:
        if(nodeOne not in self.nodes or nodeTwo not in self.nodes):
            return
        if(nodeTwo not in self.nodes[nodeOne]):
            self.nodes[nodeOne].add(nodeTwo)
        if(nodeOne not in self.nodes[nodeTwo]):
            self.nodes[nodeTwo].add(nodeOne)

class DirectedGraph(Graph):
    def addEdge(self, nodeOne, nodeTwo) -> None:
        if(nodeOne not in self.nodes or nodeTwo not in self.nodes):
            return
        if(nodeTwo not in self.nodes[nodeOne]):
            self.nodes[nodeOne].add(nodeTwo)
    
    def topologicalSort(self) -> None:
        if(not self.root):
            print('No nodes in the graph')
            return
        incomingEdges = {}
        processQueue = [self.root]
        while processQueue:
            currNode = processQueue.pop(0)
            if(currNode not in incomingEdges):
                incomingEdges[currNode] = 0
            for child in self.nodes[currNode]:
                if(child not in incomingEdges):
                    incomingEdges[child] = 1
                else:
                    incomingEdges[child] += 1
                processQueue.append(child)
        for node, inEdge in incomingEdges.items():
            if(inEdge == 0):
                processQueue.append(node)
        topoSort = []
        while processQueue:
            currNode = processQueue.pop(0)
            for child in self.nodes[currNode]:
                incomingEdges[child] -= 1
                if(incomingEdges[child] == 0):
                    processQueue.append(child)
            topoSort.append(currNode)
        if(len(topoSort) != len(self.nodes)):
            print('No topological sort')
            return
        print(f'The topological sort is: {topoSort}')
    