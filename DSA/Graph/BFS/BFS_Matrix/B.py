from collections import deque

def BFS(graph, start):
    visited = set()
    q = deque()

    visited.add(start)
    q.append(start)

    while q:
        u = q.popleft() # u is the current node being processed
        print(u, end=" ")

        for v in graph[u]: # v is a neighbor of u
            if v not in visited: # If v hasn't been visited, we mark it as visited and add it to the queue
                visited.add(v)
                q.append(v)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}

BFS(graph, 0)