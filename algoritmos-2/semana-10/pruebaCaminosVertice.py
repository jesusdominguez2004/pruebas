def dfs_all_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:
            new_paths = dfs_all_paths(graph, neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

print(f"Paths A to B: {dfs_all_paths(graph, 'A', 'B')}")
print(f"Paths A to C: {dfs_all_paths(graph, 'A', 'C')}")
print(f"Paths A to D: {dfs_all_paths(graph, 'A', 'D')}")
print(f"Paths A to E: {dfs_all_paths(graph, 'A', 'E')}")
print(f"Paths A to F: {dfs_all_paths(graph, 'A', 'F')}\n")

graph = {
    'A': ['B'],
    'B': ['C', 'E'],
    'C': ['D'],
    'D': ['A'],
    'E': ['D'],
}

print(f"Paths A to B: {dfs_all_paths(graph, 'A', 'B')}")
print(f"Paths A to C: {dfs_all_paths(graph, 'A', 'C')}")
print(f"Paths A to D: {dfs_all_paths(graph, 'A', 'D')}")
print(f"Paths A to E: {dfs_all_paths(graph, 'A', 'E')}")

