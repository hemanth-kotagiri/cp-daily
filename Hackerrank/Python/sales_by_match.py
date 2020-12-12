#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    count = 0
    pair = {}
    for color in ar:
        if color not in pair:
            pair[color] = 1
        else:
            pair[color] += 1
    for value in pair.values():
        if value > 1:
            count += value//2

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
