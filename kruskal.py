import heapq  # Importing heapq to use priority queue (min-heap)

# === Disjoint Set (Union-Find) with path compression ===
class DisjointSet:
    def __init__(self, n):
        # Initialize each node to be its own parent (separate sets)
        self.parent = list(range(n))

    def find(self, u):
        # Recursively find the representative of the set containing u
        # Apply path compression for optimization
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Find the representatives of the sets containing u and v
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            # Merge the sets by making one root the parent of the other
            self.parent[pu] = pv
            return True  # Union was successful
        return False  # Already in the same set, union not needed


# === Kruskal's Algorithm ===
def kruskal_mst(V, edges):
    # Convert list of edges to a min-heap based on edge weights
    # Edge format: (weight, u, v)
    heapq.heapify(edges)
    
    ds = DisjointSet(V)  # Create disjoint set for V vertices
    mst = []             # List to store MST edges
    mst_cost = 0         # Variable to store total weight of MST

    # Continue until all edges are processed or MST is complete (V-1 edges)
    while edges and len(mst) < V - 1:
        weight, u, v = heapq.heappop(edges)  # Extract edge with minimum weight

        # If including the edge doesn't form a cycle
        if ds.union(u, v):
            mst.append((u, v, weight))  # Add the edge to MST
            mst_cost += weight          # Add the edge's weight to total cost
    
    return mst, mst_cost


# === Input Section ===
V = int(input("Enter number of vertices: "))  # Total number of vertices
E = int(input("Enter number of edges: "))     # Total number of edges

edges = []  # List to store all edges
print("Enter edges in format: u v w")
for _ in range(E):
    u, v, w = map(int, input().split())  # Input edge between u and v with weight w
    edges.append((w, u, v))  # Store edge with weight first for heapq to prioritize by weight

# === Run Kruskal's Algorithm ===
mst, result = kruskal_mst(V, edges)

# === Output the MST result ===
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
print("Total cost of MST:", result)


# === Input Section ===
V = int(input("Enter number of vertices: "))  # Input number of vertices
E = int(input("Enter number of edges: "))     # Input number of edges

edges = []  # List to store all edges
print("Enter edges in format: u v w")
for _ in range(E):
    u, v, w = map(int, input().split())  # Input edge u -- v with weight w
    edges.append((u, v, w))

# === Run Kruskal's Algorithm ===
mst, result = kruskal_mst(V, edges)

# === Output the MST result ===
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
print("Total cost of MST:", result)

# Enter number of vertices: 5
# Enter number of edges: 7
# Enter edges in format: u v w
# 0 1 10
# 0 2 6
# 0 3 5
# 1 3 15
# 2 3 4
# 1 4 7
# 2 4 8
