#https://www.hackerrank.com/challenges/sparse-arrays/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    # Hash the strings
    hash_map = {}
    for string in strings:
        if string in hash_map:
            hash_map[string] += 1
        else:
            hash_map[string] = 1
    results = []
    for query in queries:
        if query in hash_map:
            results.append(hash_map[query])
        else: results.append(0)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
