import heapq  # Import heapq for priority queue implementation (min-heap)

# Function to perform Prim's algorithm for Minimum Spanning Tree
def prim_mst(V, edges):
    # Create adjacency list to represent the undirected weighted graph
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))  # Add edge u -> v with weight w
        adj[v].append((u, w))  # Add edge v -> u (since the graph is undirected)

    visited = [False] * V      # Track visited nodes
    min_heap = [(0, 0)]        # Priority queue initialized with (weight=0, node=0)
    total_cost = 0             # To store the total cost of the MST

    # Process the heap until all reachable nodes are visited
    while min_heap:
        weight, node = heapq.heappop(min_heap)  # Get the edge with the minimum weight
        if visited[node]:
            continue  # Skip if already visited
        visited[node] = True  # Mark current node as visited
        total_cost += weight  # Add weight to total MST cost

        # Check all neighbors of the current node
        for neighbor, edge_weight in adj[node]:
            if not visited[neighbor]:
                # If the neighbor is not visited, push the edge to the heap
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return total_cost  # Return the final MST cost

# === Input Section ===
V = int(input("Enter number of vertices: "))  # Number of vertices
E = int(input("Enter number of edges: "))     # Number of edges

edges = []  # List to hold all edges
print("Enter edges in format: u v w")
for _ in range(E):
    u, v, w = map(int, input().split())  # Input each edge
    edges.append((u, v, w))

# === Run Prim's Algorithm ===
result = prim_mst(V, edges)  # Compute the MST cost
print("Cost is:", result)    # Output the total MST cost

#Enter number of vertices: 5
# Enter number of edges: 7
# Enter edges in format: u v w
# 0 1 2
# 0 3 6
# 1 2 3
# 1 3 8
# 1 4 5
# 2 4 7
# 3 4 9
