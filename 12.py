# Graph representation
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}


def bfs(queue, visited):
    if queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue += graph[node]

        bfs(queue, visited)
    return visited


print("BFS Traversal Order from A is:", bfs(["A"], []))
