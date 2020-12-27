# This problem was asked by Pivotal.
# Write an algorithm that finds the total number of set bits in all integers between 1 and N.

def getSetBitsOf(num):
    return bin(num)[2:].count("1")

def solution(n):
    total = 0
    for i in range(1, n + 1):
        total += getSetBitsOf(i)
    return total


print(solution(3)) # 4
print(solution(6)) # 9
print(solution(8)) # 13
