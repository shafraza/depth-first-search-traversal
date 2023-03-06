# Graph Data Structure and DFS Traversal
# By Shafaqat Ali (@shafraza)


# Class definition for a graph data structure
class Graph:
    # Constructor to initialize the graph
    def __init__(self):
        # A dictionary to hold the graph data
        self.graph = {}

    # Method to add an edge to the graph
    def add_edge(self, node, edges):
        # Add the node and its edges to the graph
        self.graph[node] = edges

    # Method to perform DFS traversal on the graph
    def dfs(self, start_node):
        # Set to keep track of visited nodes
        visited = set()
        # Stack to hold nodes to be visited
        stack = [start_node]
        # List to hold the order of visited nodes
        result = []

        # Loop until the stack is empty
        while stack:
            # Pop a node from the stack
            node = stack.pop()

            # If the node has not been visited
            if node not in visited:
                # Add it to the visited set and the result list
                visited.add(node)
                result.append(node)

                # Loop through the neighbors of the node
                for neighbor in self.graph[node]:
                    # If the neighbor has not been visited, add it to the stack
                    if neighbor not in visited:
                        stack.append(neighbor)

        # Return the list of visited nodes in the order they were visited
        return result

# Ask the user for input
n = int(input("Enter the number of edges: "))
g = Graph()

# Loop to get user input for edges
for i in range(n):
    node = input("Enter the starting node of edge {}: ".format(i+1))
    edges = input("Enter the edges of {}: ".format(node)).split()
    g.add_edge(node, edges)

# Ask the user for the starting node of the DFS traversal
start_node = input("Enter the starting node for DFS traversal: ")

# Perform DFS traversal and print the output
dfs_result = g.dfs(start_node)
print("DFS Traversal starting from node {}: {}".format(start_node, dfs_result))
