# Node class that represents a node in a graph
# Each node has a value and an Adjaceny List of its children nodes
class GraphNode:
  def __init__(self, value=0):
    self.children = []
    self.value = value

# Graph class that contains a list of GraphNodes
# Which represents all the nodes in a graph
class Graph:
  def __init__(self):
    self.nodes = []
    self.visited = set()
  
  # This function will use Breadth First Search on the root of the graph
  # clears the visited set after the search is complete so more search
  # functions can be called
  def rootBFS(self):
    if(len(self.nodes) != 0):
      self.breadthFirstSearch(self.nodes[0])
    else:
      return False
    self.visited.clear()
  
  # This function will use Depth First Search on the root of the graph
  # clears the visited set after the search is complete so more search
  # functions can be called
  def rootDFS(self):
    if(len(self.nodes) != 0):
      self.depthFirstSearch(self.nodes[0])
    else:
      return False
    self.visited.clear()

  # Depth First Search function that visits as far down from the 
  # inputted node as possible then backtracks on the graph
  # This means the algorithm explores on node in each level of the graph
  # first then once there are no more nodes left to visit, it will backtrack
  # and visit the previous level of the graph
  # O(V + E) runtime where V is the number of nodes in the graph
  # and E are the total edges. Visitng all edges in the graph
  # is necessary to determine if a node is already in the visited set
  def depthFirstSearch(self, node):

    # Make sure the inputted node is a GraphNode
    # Or if it is empty (no more nodes to visit) return back to the function
    if(isinstance(node, GraphNode) == False or node == None):
      return False

    # Else mark the current node as visited and print
    # Then for each child of the node recurse the depth first search
    # this means the first child's subtree will be visited before
    # the next child is explored and so on
    else:
      self.visited.add(node)
      print(node.value)
      for child in node.children:
        if(child not in self.visited):
          self.depthFirstSearch(child)

  # Breadth First Search algorithm that will visit each node on a level
  # of a graph before moving on to the next level of the graph
  # In other words, all children of a node will be visited before the children's
  # children are visited. BFS is implemented with a priority queue to 
  # determine the next node to visit
  # O(V + E) runtime where V is the total nodes in the graph
  # and E is the total number of edges in the graph
  # all edges must be visited to determine if a node has been visited
  def breadthFirstSearch(self, node):

    # Make sure the inputted node is a GraphNode
    # Or if it is empty (no more nodes to visit) return back to the function
    if(isinstance(node, GraphNode) == False or node == None):
      return False

    else:

      # Queue that will hold the next node to visit
      nodeQueue = []

      # Add the inputted starting node of the search to the queue
      nodeQueue.append(node)

      # Set that will hold nodes that have been pushed to the queue
      # This is necessary if different nodes have the same unvisited child
      # if this set was missing, both nodes would add this node to the queue
      accountedFor = set()

      # While the queue is not empty, dequeue the top element of the queue
      # mark this node as visited and print
      # then add all the unvisited and unaccounted for children to the queue
      # as they will be the next to visit (children visited before next level of graph)
      while(len(nodeQueue) != 0):
        tempNode = nodeQueue.pop(0)
        self.visited.add(tempNode)
        print(tempNode.value)
        for child in tempNode.children:
          if(child not in self.visited and child not in accountedFor):
            nodeQueue.append(child)
            accountedFor.add(child)

    # Since this function is iterative we can clear the visited set after
    self.visited.clear()

  # Function to run a topological sort on the graph
  # For a graph to have a topological sort, it must be directed and acyclic
  # If the graph has cycles or is not directed, this function will return False
  # A topological sort is one in which each node in the sorted list comes before
  # the next nodes in the list. In other words if there is an edge in the graph
  # between a to b, and b to c, then a will appear before b in the list, and 
  # b will appear before c, therefore a is beore c. Runtime O(V + E)
  def topologicalSort(self):

    # queue that will contain the order of the sort
    orderOfSort = []

    # queue that will contain the next node to process
    processQueue = []

    # dictionary to count each node's incoming edges (number of nodes that point to it)
    inboundCounts = {}

    # Loop through all nodes in the graph
    # add node to inboundCounts dict if not in already, set incoming edges to 0
    # loop through all the children of the node and add one to their incoming count
    # or add to dict if not in already. This runs in O(V + E) because at each node
    # each of its edges are explored. All nodes and edges are visited
    for node in self.nodes:
      if(node not in inboundCounts):
        inboundCounts[node] = 0
      for child in node.children:
        if(child not in inboundCounts):
          inboundCounts[child] = 1
        else:
          inboundCounts[child] += 1
    
    # Add each node with no inbound edges to the process queue
    # the ordering of these nodes does not matter as they
    # don't depend on any other nodes and will be processed first. O(V) runtime
    for key, value in inboundCounts.items():
      if(value == 0):
        processQueue.append(key)

    # while there are nodes in the process queue
    # pop the first element from the queue
    # since we will add this node to the order queue, we can process the children nodes
    # and remove 1 from their inbound nodes count since the parent has already been processed
    # this is because we have guaranteed that the children's parent comes before them in the sort
    # if the incoming edge count of the child is 0, we can add it to the process queue because
    # it no longer depends on other nodes
    # This runs in O(V + E)
    while(len(processQueue) != 0):
      tempNode = processQueue.pop(0)
      for child in tempNode.children:
        inboundCounts[child] -= 1
        if(inboundCounts[child] == 0):
          processQueue.append(child)
      orderOfSort.append(tempNode)

    # Each node has to be processed for a topological sort to be successful
    # if the order is missing nodes, it means that there are nodes in the graph
    # have cycles. This is at some point in the sort, the process queue will be empty
    # due to a the queue already being empty and the node not having 0 remaining incoming edges
    if(len(orderOfSort) == len(self.nodes)):
      return orderOfSort
    else:
      return False