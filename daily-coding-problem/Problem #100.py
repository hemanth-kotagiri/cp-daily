def MinimumPath(array):
    count = 0
    for i in range(len(array)-1):
        current = array[i]
        n = array[i+1]
        count+= max(abs(current[0]-n[0]),abs(current[1]-n[1]))
    return count

array = [(0, 0), (1, 1), (1, 2)] ## OP: 2

print(MinimumPath(array))