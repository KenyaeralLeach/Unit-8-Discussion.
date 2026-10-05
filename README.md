# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using **Breadth-First Search (BFS)**. BFS visits graph nodes level by level, starting from a selected node.

## Learning Objectives

* Represent graphs using adjacency lists.
* Implement Breadth-First Search.
* Use queues in graph traversal.
* Track visited nodes.
* Analyze graph traversal behavior.
* Understand BFS compared with Depth-First Search (DFS).
* Handle graph edge cases.

## Requirements

### 1. Create a Graph

The program creates a graph using an adjacency list. The example graph represents relationships between users in a streaming platform.

The graph contains at least six nodes and multiple connections between nodes.

### 2. Perform BFS Traversal

The `bfs()` function performs Breadth-First Search using Python's `deque` as a queue.

The algorithm:

1. Starts from a selected node.
2. Adds the starting node to the queue.
3. Removes the first node from the queue.
4. Visits its unvisited neighbors.
5. Adds those neighbors to the queue.
6. Continues until the queue is empty.

A `visited` set prevents the same node from being processed repeatedly.

### 3. Add Nodes or Edges

The program adds an additional user/node and connects it to the existing graph. BFS is then performed again to demonstrate how the traversal changes.

### 4. Demonstrate Edge Cases

The program demonstrates several edge cases:

* Starting from a different node.
* A disconnected graph.
* A missing starting node.
* A graph containing only one node.
* An empty graph.

The program handles these cases safely without crashing.

### 5. Analyze BFS Behavior

BFS explores nodes level by level. This makes it useful when the closest or shortest connection is important.

For an unweighted graph, BFS can be used to find the shortest number of edges between two nodes.

### 6. Real-World Graph Example

The example represents a simplified streaming recommendation system.

* Nodes represent users.
* Edges represent shared viewing preferences.
* BFS can explore recommendations starting with users who are directly connected before moving farther through the network.

## BFS vs. DFS

### BFS

BFS explores the graph level by level and uses a queue.

It is useful for:

* Shortest paths in unweighted graphs.
* Finding nearby connections.
* Level-order exploration.
* Social network connections.

### DFS

DFS explores as deeply as possible along one path before backtracking. It commonly uses recursion or a stack.

It is useful for:

* Exploring connected components.
* Maze solving.
* Backtracking problems.
* Exploring deep paths in a graph.

### When to Use BFS

BFS is preferred when the distance from the starting node matters or when we want to find the shortest path in an unweighted graph.

### When to Use DFS

DFS is preferred when the goal is to explore deeply into a graph or when a problem naturally involves backtracking.

## Discussion Board Reflection

While completing this assignment, I learned how to represent graphs with adjacency lists, implement BFS, use a queue for traversal, and track visited nodes. I also learned why BFS visits nodes level by level and how this behavior differs from DFS.

One challenge was preventing nodes from being visited repeatedly when the graph contained cycles or multiple connections. I solved this by using a `visited` set. I also tested different starting nodes and edge cases such as an empty graph and a missing starting node.

BFS and DFS both traverse graphs, but they use different strategies. BFS explores all nearby nodes before moving farther away, while DFS follows one path as deeply as possible before backtracking. BFS is useful for shortest paths in unweighted graphs and finding nearby connections. DFS is useful for maze solving, connected components, and problems involving backtracking.

Overall, this assignment helped me understand how the choice of traversal strategy depends on the structure and goal of a graph problem.

## How to Run

Run the following command from the terminal:

```bash
python unit8_discussion.py
```

The program displays:

* The graph structure.
* The initial BFS traversal.
* The updated graph after adding a node/edge.
* The updated BFS traversal.
* Results for multiple edge cases.
