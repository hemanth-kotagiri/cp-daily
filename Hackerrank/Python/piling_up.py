# Enter your code here. Read input from STDIN. Print output to STDOUT

def checkValidPair(cubes, stack, left, right, no):
    if len(stack) == 0:
        if cubes[left] > cubes[right]:
            stack.append(cubes[left])
            stack.append(cubes[right])
        else:
            stack.append(cubes[right])
            stack.append(cubes[left])
    else:
        if cubes[left] >= cubes[right] and cubes[left] < stack[-1]:
            stack.append(cubes[left])
            stack.append(cubes[right])
        elif cubes[right] > cubes[left] and cubes[right] < stack[-1]:
            stack.append(cubes[right])
            stack.append(cubes[left])
        else:
            no = True




res = []
for T in range(int(input())):
    no = False
    n = int(input())
    cubes = list(map(int, input().split()))
    stack = []
    start, end = 0, len(cubes) - 1
    while start < end:
        checkValidPair(cubes, stack, start, end, no)
        print(stack)
        if no:
            res.append("NO")
            break
        else:
            start += 1
            end -= 1
    if (start == end and cubes[start] > stack[-1]):
        res.append("NO")
    if not no and len(stack) == len(cubes):
        res.append("YES")
    print(res)

for resp in res:
    print(resp)



    # if len(cubes) % 2 != 0:
    #     # Case when there is left a last element which is middle
    #     middleIdx = len(cubes) // 2
    #     middleElem = cubes[middleIdx]
    #     if middleElem > cubes[middleIdx - 1] and middleElem > cubes[middleIdx + 1]:
    #         print("NO")
    # print("YES")

    # startingPointer, endingPointer = 1, len(cubes) - 2

    # while startingPointer != endingPointer:
    #     if cubes[startingPointer] == cubes[endingPointer] and cubes[startingPointer] < stack[-1]:
    #         stack.append(cubes[startingPointer])
    #         stack.append(cubes[endingPointer])

    #         startingPointer += 1
    #         endingPointer -= 1

    #     elif cubes[startingPointer] > cubes[endingPointer] and cubes[startingPointer] < stack[-1]:
    #         stack.append(cubes[startingPointer])
    #         stack.append(cubes[endingPointer])

    #         startingPointer += 1
    #         endingPointer -= 1
    #     elif cubes[startingPointer] < cubes[endingPointer] and cubes[endingPointer] < stack[-1]:
    #         stack.append(cubes[startingPointer])
    #         stack.append(cubes[endingPointer])

    #         startingPointer += 1
    #         endingPointer -= 1
    #     else:
    #         print("NO")
    #         no = True
    #         break
    # if not no: print("YES")
