graph = {
    "A" : [("B",1),("C",4)],
    "B" : [("D",5)],
    "C" : [("D",1)],
    "D" : []
}

heuristic = {"A":6,"B":4,"C":1,"D":0}

def gbf(start,goal):
    visited = set()
    queue = [[start]]

    while queue:
        queue.sort(key=lambda path:heuristic[path[-1]])
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor,cost in graph[node]:
                queue.append(path+[neighbor])
    return None

solution = gbf("A","D")
print(f"Greedy Best First Search Path: {solution}")
