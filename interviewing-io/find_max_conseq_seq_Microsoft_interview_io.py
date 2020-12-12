# Given a list of integers L, find the maximum length of a sequence of conecutive
# numbers that can be formed using elements from L.
# EG: given [6, 5, 2, 99, 3, 4, 1, 100] => max(|{99, 100}, {1...6}|) = 6

# TODO: Make this a recursive solution

def no_knowledge_solution(array):
    highestSequenceLength = 0
    currentSequenceLength = 0

    i = 0
    j = 0
    visited = []
    while i < len(array):
        currentElement = array[i]
        if currentElement not in visited:

            # print(currentElement)

            if currentElement - 1 in array:
                currentSequenceLength += 1
                i = array.index(currentElement - 1)
                visited.append(currentElement)
                # print("seq:", currentSequenceLength)

            elif currentElement + 1 in array:
                currentSequenceLength += 1
                i = array.index(currentElement + 1)
                visited.append(currentElement)
                if currentElement == 4:
                    print(visited)
                    print("i:", i, "j:", j)
                # print("seq:", currentSequenceLength)

            else:
                if currentSequenceLength > highestSequenceLength:
                    highestSequenceLength = currentSequenceLength
                    # print("seq:", currentSequenceLength)
                currentSequenceLength = 0
                j += 1
                i = j
                visited = list()
        else:
            if currentSequenceLength > highestSequenceLength:
                print("curr_seq: ", currentSequenceLength)
                highestSequenceLength = currentSequenceLength
                # print("seq:", currentSequenceLength)
            currentSequenceLength = 0
            j += 1
            i = j

    return highestSequenceLength

def sortSolution(arr):
    temp = sorted(arr)
    total_max = 0
    max_sub_arr = []
    for i in range(len(temp) - 1):
        if temp[i] + 1 == temp[i + 1]:
            max_sub_arr.append(temp[i])
        else:
            if len(max_sub_arr) + 1 > total_max: total_max = len(max_sub_arr) + 1
    
    return total_max


arr = [6, 5, 2, 99, 3, 4, 1, 100]  # 6
arr2 = [1, 94, 93, 1000, 5, 92, 78]  # 3
arr3 = [1, 5, 92, 4, 78, 6, 7]  # 4

# print(no_knowledge_solution(arr))
# print(no_knowledge_solution(arr2))
# print(no_knowledge_solution(arr3))
print(sortSolution(arr))
print(sortSolution(arr2))
print(sortSolution(arr3))
