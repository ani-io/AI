import heapq  # For priority queue

def dijkstra(V, edges, start):
    # Build adjacency list
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))  # If undirected; remove if directed

    # Distance array to store shortest distance from source
    dist = [float('inf')] * V
    dist[start] = 0

    # Min-heap to select the edge with the minimum weight
    min_heap = [(0, start)]  # (distance, node)

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        # Skip if we have already found a better path
        if current_dist > dist[u]:
            continue

        # Traverse through neighbors
        for neighbor, weight in adj[u]:
            #dist[v] = dist[u] + weight[u][v]
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                heapq.heappush(min_heap, (dist[neighbor], neighbor))

    return dist

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []
print("Enter edges in format: u v w")
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

start = int(input("Enter the source vertex: "))

# Run Dijkstra's algorithm
shortest_distances = dijkstra(V, edges, start)

# Output the result
print(f"Shortest distances from vertex {start}:")
for i, d in enumerate(shortest_distances):
    print(f"To vertex {i} => Distance: {d}")


# Enter number of vertices: 5
# Enter number of edges: 6
# Enter edges in format: u v w
# 0 1 2
# 0 3 6
# 1 2 3
# 1 3 8
# 1 4 5
# 2 4 7
# Enter the source vertex: 0
