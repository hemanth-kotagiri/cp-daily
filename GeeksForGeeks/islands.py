# Find the number of islands. Group of connected 1s are islands
""" 
Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1} 
Output : 5
"""

def find_connected_verticies(matrix, visited, i, j, number_of_islands):
    connectedNodes = [[i, j]]
    while len(connectedNodes):
        currentNode = connectedNodes.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        allConnectedNodes = getConnections(matrix, visited, i, j)
        for node in allConnectedNodes:
            connectedNodes.append(node)


def getConnections(matrix, visited, i, j):
    totalConnections = []
    if i > 0 and not visited[i - 1][j]:
        totalConnections.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        totalConnections.append([i + 1, j])
    
    if j > 0 and not visited[i][j-1]:
        totalConnections.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        totalConnections.append([ i, j + 1 ])
    
    if i < len(matrix) - 1 and j>0 and not visited[i+1][j-1]:
        totalConnections.append([i+1, j-1])

    if i < len(matrix) - 1 and j<len(matrix[0])-1 and not visited[i+1][j+1]:
        totalConnections.append([i+1, j+1])
    
    return totalConnections





def solution(matrix):
    number_of_islands = 0
    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            if matrix[i][j] == 1: number_of_islands += 1
            find_connected_verticies(matrix, visited, i, j, number_of_islands)
    
    return number_of_islands


mat = [[ 1, 1, 0, 0, 0 ],
       [ 0, 1, 0, 0, 1 ],
       [ 1, 0, 0, 1, 1 ],
       [ 0, 0, 0, 0, 0 ],
       [ 1, 0, 1, 0, 1 ]]

mat2 = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]

mat3 = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]

print(solution(mat))