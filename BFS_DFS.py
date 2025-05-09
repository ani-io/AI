def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    graph = {} #directory which consists node as keys and neighbors as values
    n = int(input("no of nodes: "))
    for i in range(1, n + 1):
        graph[i] = []
        for x in map(int, input(f"the neighbors of {i} (space-separated): ").split()):
            graph[i].append(x)
            if x not in graph:
                graph[x] = []
            graph[x].append(i)  # ensure undirected connection

    while True:
        print("\nMenu:")
        print("1. DFS")
        print("2. BFS")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start = int(input("Enter starting node for DFS: "))
            print("DFS traversal:", end=" ")
            dfs(graph, start, set())
            print()
        elif choice == "2":
            start = int(input("Enter starting node for BFS: "))
            print("BFS traversal:", end=" ")
            bfs(graph, start)
            print()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()

#      1
#     / \
#    2   4
#   / \
#  3   5
#     /
#    6  
# no of nodes: 6
# the neighbors of 1 (space-separated): 2 4
# the neighbors of 2 (space-separated): 1 3 5
# the neighbors of 3 (space-separated): 2 
# the neighbors of 4 (space-separated): 1 
# the neighbors of 5 (space-separated): 2 6
# the neighbors of 6 (space-separated): 5
# the start node is: 1
# dfs 1 2 3 5 6 4 
# bfs 1 2 4 3 5 6