def traverseNode(matrix, visited_matrix, i, j, sizes):
    currentSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited_matrix[i][j]:
            continue
        visited_matrix[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(matrix, visited_matrix, i, j)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
    if currentSize > 0: sizes.append(currentSize)


def getUnvisitedNeighbours(matrix, visited_matrix, i, j):
    unvisitedNeighbours = []
    if i > 0 and not visited_matrix[i - 1][j]:
        unvisitedNeighbours.append([i-1, j])
    if i < len(matrix) - 1 and not visited_matrix[i + 1][j]:
        unvisitedNeighbours.append([i + 1, j])
    if j > 0 and not visited_matrix[i][j -1]:
        unvisitedNeighbours.append([i, j - 1])
    if j < len(matrix[i]) - 1 and not visited_matrix[i][j + 1]:
        unvisitedNeighbours.append([i, j + 1])
    
    return unvisitedNeighbours


def riverSizes(matrix):
    sizes = []
    visited_matrix = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited_matrix[i][j]:
                continue
            traverseNode(matrix, visited_matrix, i, j, sizes)
    
    return sizes


matrix = [
[1, 0, 0, 1, 0],
[1, 0, 1, 0, 0],
[0, 0, 1, 0, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 0]]

print("Hello")
print(riverSizes(matrix))