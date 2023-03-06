<h1>Problem Statement</h1>
	<h2>Implement a Graph Data Structure and Perform Depth-First Search Traversal</h2>
	<h3>Problem Description</h3>
	<p>In this problem, you are required to implement a graph data structure and perform Depth-First Search (DFS) traversal on it using Python. You are required to define a <code>Graph</code> class that represents the graph data structure, and implement the following methods:</p>
	<ul>
		<li><code>__init__</code>: Initializes an empty graph dictionary.</li>
		<li><code>add_edge</code>: Adds an edge to the graph. It takes in a <code>node</code> parameter representing the starting node of the edge, and an <code>edges</code> parameter representing the list of edges that the starting node connects to.</li>
		<li><code>dfs</code>: Implements the Depth First Search (DFS) algorithm for graph traversal. It takes in a <code>start_node</code> parameter representing the starting node for the traversal. The algorithm starts by initializing a <code>visited</code> set to keep track of the visited nodes, a <code>stack</code> to hold the nodes to be visited, and a <code>result</code> list to hold the order of visited nodes.</li>
	</ul>
	<p>Your implementation of the DFS algorithm should be able to traverse the entire graph and return a list of visited nodes in the order they were visited.</p>
  <h3>Input</h3>
<p>The input to the program consists of the following:</p>
<ul>
	<li>The number of edges in the graph, <code>n</code> (1 ≤ <code>n</code> ≤ 100).</li>
	<li><code>n</code> lines of input, each containing two space-separated strings, <code>node</code> and <code>edges</code>, representing an edge in the graph. <code>node</code> represents the starting node of the edge, and <code>edges</code> is a space-separated list of strings representing the edges that <code>node</code> connects to.</li>
	<li>The starting node for the DFS traversal, a string <code>start_node</code>.</li>
</ul>

<h3>Output</h3>
<p>The output of the program consists of the following:</p>
<ul>
	<li>The order of visited nodes during the DFS traversal, a list of strings.</li>
</ul>

<h3>Constraints</h3>
<ul>
	<li>The strings <code>node</code> and <code>edges</code> contain only alphabetical characters and have length at most 10.</li>
	<li>The graph is connected, i.e., every node can be reached from every other node.</li>
	<li>There are no self-loops in the graph, i.e., an edge cannot connect a node to itself.</li>
	<li>The starting node for the DFS traversal is a valid node in the graph.</li>
</ul>

<h3>Conclusion</h3>
<p>In this problem, you implemented a graph data structure and performed Depth-First Search (DFS) traversal on it using Python. You defined a <code>Graph</code> class that represents the graph data structure and implemented
