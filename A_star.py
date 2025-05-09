import heapq

# Heuristic function: Manhattan Distance between two points
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# A* Search Algorithm implementation
def a_star(grid, start, goal):
    n, m = len(grid), len(grid[0])  # Dimensions of the grid
    visited = [[False] * m for _ in range(n)]  # 2D array to mark visited cells
    heap = []  # Min-heap to store nodes with priority based on f = g + h

    sx, sy = start  # Start coordinates
    gx, gy = goal   # Goal coordinates

    g = 0  # Cost from start to current node
    h = heuristic(sx, sy, gx, gy)  # Heuristic cost from current to goal
    f = g + h  # Total estimated cost

    heapq.heappush(heap, (f, g, sx, sy))  # Push starting node to heap

    # Possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        # Pop the node with the lowest estimated total cost (f)
        f, g, x, y = heapq.heappop(heap)

        # Skip if already visited
        if visited[x][y]:
            continue

        visited[x][y] = True  # Mark node as visited

        # Check if we've reached the goal
        if (x, y) == (gx, gy):
            print(f"Reached goal with cost: {g}")
            return

        # Explore all valid neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Ensure the new cell is within bounds, not visited, and not an obstacle
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 0:
                new_g = g + 1  # Cost increases by 1 for each move
                new_h = heuristic(nx, ny, gx, gy)  # Recalculate heuristic
                new_f = new_g + new_h  # New estimated total cost
                heapq.heappush(heap, (new_f, new_g, nx, ny))  # Push neighbor to heap

    # If the loop ends and we didn't reach the goal
    print("Goal not reachable!")

# Example grid (0 = open, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Start position
goal = (3, 3)   # Goal position

# Run A* algorithm
a_star(grid, start, goal)
