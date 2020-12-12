# https://www.hackerrank.com/challenges/2d-array/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys


def bfs(arr, i, j):
    curr_sum = arr[i][j]
    # Top
    curr_sum += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
    # Bottom
    curr_sum += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]

    return curr_sum

# Complete the hourglassSum function below.


def hourglassSum(arr):
    # 2D array.
    max_sum = float("-inf")
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            # BFS
            curr_sum = bfs(arr, i, j)
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
