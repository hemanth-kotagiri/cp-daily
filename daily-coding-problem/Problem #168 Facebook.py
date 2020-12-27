"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]


 Follow-up: What if you couldn't use any extra space?"""

from random import randint


def solution(mat):
    # for row in mat:
    # print(row)
    # print("-"*50)
    answer = list()
    current = list()
    for i in range(len(mat)):
        temp = 0
        for _ in range(len(mat)):
            current.insert(0, mat[temp][i])
            temp += 1
        answer.append(current)
        current = []
    # for row in answer:
        # print(row)

    return answer


mat = [[1, 2, 3, 4],
       [4, 5, 6, 4],
       [7, 8, 9, 4],
       [1, 2, 3, 4]]

mat2 = [[1, 2],
        [4, 5]]

mat3 = [[randint(1, 100) for i in range(4)] for i in range(4)]


assert solution(mat2) == [[4, 1],
                          [5, 2]]
