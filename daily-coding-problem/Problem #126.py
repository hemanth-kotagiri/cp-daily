def rotateList(array, k):
    while k > 0:
        if k > len(array):
            k -= int((k/len(array))-1)*len(array)
            continue
        array.append(array[0])
        del array[0]
        k -= 1
    return array


array, k = [1, 2, 3, 4, 5, 6, ], 2
print(rotateList(array, k))
