"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

This program demonstrates Breadth-First Search using a graph
represented by an adjacency list.

The example uses a simplified streaming recommendation
system where nodes represent users and edges represent
shared viewing preferences.
===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on a graph.

    Parameters:
        graph: Dictionary representing the graph as an
               adjacency list.
        start: Node where the traversal begins.

    Returns:
        A list containing nodes in BFS traversal order.

    BFS uses a queue because nodes should be processed in
    the same order that they are discovered.

    A visited set prevents nodes from being visited more
    than once, which is especially important when the graph
    contains cycles or multiple connections.
    """

    # Handle an empty graph safely.
    if not graph:
        return []

    # Handle a starting node that does not exist.
    if start not in graph:
        return []

    # Queue stores nodes waiting to be processed.
    queue = deque([start])

    # Track nodes that have already been discovered.
    visited = {start}

    # Store the final traversal order.
    traversal_order = []

    while queue:
        # Remove the first node from the queue.
        current = queue.popleft()

        # Add the node to the traversal result.
        traversal_order.append(current)

        # Add unvisited neighbors to the queue.
        #
        # Because BFS uses a queue, these neighbors will
        # be processed after the nodes already waiting in
        # the queue. This creates the level-by-level behavior.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # =====================================================
    # CREATE A GRAPH
    # =====================================================
    #
    # This graph represents a simplified streaming platform.
    #
    # Each node represents a user.
    # An edge means two users have shared viewing preferences.
    #
    # The graph is represented using an adjacency list.

    graph = {
        "Alice": ["Bob", "Charlie"],
        "Bob": ["Alice", "David", "Eve"],
        "Charlie": ["Alice", "Frank"],
        "David": ["Bob", "Eve"],
        "Eve": ["Bob", "David", "Frank"],
        "Frank": ["Charlie", "Eve"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # =====================================================
    # BFS TRAVERSAL
    # =====================================================

    print("\n=== BFS TRAVERSAL ===")

    start_node = "Alice"
    traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print("BFS traversal:", " -> ".join(traversal))

    print(
        "\nBFS visits Alice first, then Alice's immediate "
        "connections, and then moves to the next level."
    )

    # =====================================================
    # ADD A NODE / EDGE
    # =====================================================

    print("\n=== UPDATED GRAPH ===")

    # Add a new user.
    graph["Grace"] = ["Frank"]

    # Add Grace as a connection of Frank.
    graph["Frank"].append("Grace")

    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # Perform BFS again after modifying the graph.
    updated_traversal = bfs(graph, start_node)

    print("\nBFS after adding Grace:")
    print(" -> ".join(updated_traversal))

    # =====================================================
    # EDGE CASE 1: DIFFERENT STARTING NODE
    # =====================================================

    print("\n=== EDGE CASE 1: DIFFERENT STARTING NODE ===")

    different_start = "David"
    result = bfs(graph, different_start)

    print(f"Starting node: {different_start}")
    print("BFS traversal:", " -> ".join(result))

    print(
        "The traversal order changes because BFS begins "
        "from a different node."
    )

    # =====================================================
    # EDGE CASE 2: DISCONNECTED GRAPH
    # =====================================================

    print("\n=== EDGE CASE 2: DISCONNECTED GRAPH ===")

    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"]
    }

    print("Graph:", disconnected_graph)

    result = bfs(disconnected_graph, "A")

    print("Starting node: A")
    print("BFS traversal:", " -> ".join(result))

    print(
        "BFS only visits the connected component containing "
        "the starting node. C and D are not reached."
    )

    # =====================================================
    # EDGE CASE 3: MISSING START NODE
    # =====================================================

    print("\n=== EDGE CASE 3: MISSING START NODE ===")

    missing_start = "Unknown"
    result = bfs(graph, missing_start)

    print(f"Starting node: {missing_start}")
    print("BFS traversal:", result)

    print(
        "The starting node does not exist, so the function "
        "returns an empty list instead of crashing."
    )

    # =====================================================
    # EDGE CASE 4: SINGLE-NODE GRAPH
    # =====================================================

    print("\n=== EDGE CASE 4: SINGLE-NODE GRAPH ===")

    single_node_graph = {
        "OnlyUser": []
    }

    result = bfs(single_node_graph, "OnlyUser")

    print("Graph:", single_node_graph)
    print("BFS traversal:", result)

    print(
        "A graph with one node returns that node because "
        "there are no neighbors to visit."
    )

    # =====================================================
    # EDGE CASE 5: EMPTY GRAPH
    # =====================================================

    print("\n=== EDGE CASE 5: EMPTY GRAPH ===")

    empty_graph = {}

    result = bfs(empty_graph, "A")

    print("Graph:", empty_graph)
    print("BFS traversal:", result)

    print(
        "The empty graph returns an empty list and does not "
        "cause an error."
    )

    # =====================================================
    # BFS VS DFS
    # =====================================================

    print("\n=== BFS ANALYSIS ===")

    print(
        "BFS explores a graph level by level using a queue."
    )

    print(
        "BFS is useful for finding the shortest path in an "
        "unweighted graph and for finding nearby connections."
    )

    print(
        "DFS explores as deeply as possible along one path "
        "before backtracking. DFS commonly uses recursion "
        "or a stack."
    )

    print(
        "For this recommendation example, BFS is useful when "
        "nearby or directly connected users should be explored "
        "before users that are farther away."
    )


if __name__ == "__main__":
    main()