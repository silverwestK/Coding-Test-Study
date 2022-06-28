#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    vertices = {start}
    result = 0
    edges.sort(key=lambda e: e[2])
    while len(vertices) < n:
        for e in edges:
            if ((e[0] in vertices and e[1] not in vertices)
                    or (e[1] in vertices and e[0] not in vertices)):
                vertices.update(e[:2])
                result += e[2]
                break
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
