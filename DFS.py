def dfs_path_planning(graph, start, end):
    stack = [[start]]
    visited = set([start])
    while stack:
        path = stack.pop()
        current=path[-1]
        if current == end:
            return path
        for neighbor in (graph[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(path +[neighbor])
    return "No path found" 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F'],
    'F': ['E']
}
start = 'A'
end = 'E'

path = dfs_path_planning(graph, start, end)

if path == "No path found":
    print("No path Found")
    
else:
    print(f"Path found from{start} to {end}:{path}")
