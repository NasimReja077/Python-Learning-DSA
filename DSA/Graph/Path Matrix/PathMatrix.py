def warshall(adj_matrix):
    n = len(adj_matrix)
    
    # Step 1: Copy adjacency matrix to path matrix
    path = [row[:] for row in adj_matrix]
    
    # Step 2: Apply Warshall's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                path[i][j] = path[i][j] or (path[i][k] and path[k][j])
    
    return path


# -------- Example --------
adj_matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]

result = warshall(adj_matrix)

print("Path Matrix:")
for row in result:
    print(row)