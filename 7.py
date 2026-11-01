
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 5)],
    "C": [("D", 1)],
    "D": []
}

h = {"A": 6, "B": 4, "C": 1, "D": 0}


def a_star(start, goal):
    visited = set()
    queue = [(h[start], 0, [start])]

    while queue:
        queue.sort(key=lambda item: item[0])
        f, g, path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path, g

        if node not in visited:
            visited.add(node)

            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    new_g = g + cost
                    new_f = new_g + h[neighbor]
                    queue.append((new_f, new_g, path + [neighbor]))

    return None, float("inf")


optimal_path, total_cost = a_star("A", "D")

print(f"Optimal A* Path: {optimal_path}")
print(f"Total Path Cost: {total_cost}")
