#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def find_max_region(matrix):
    # Write your code here
    max_region_count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                now_cell_count = count_region_cell(matrix, row, col)
                max_region_count = max(max_region_count, now_cell_count)
    return max_region_count

def count_region_cell(matrix, row, col):
    if any([row <0, col<0, row>=len(matrix), col>=len(matrix[0])]):
        return 0
    if matrix[row][col] == 0:
        return 0
    cell_count = 1
    matrix[row][col] = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if any([r!= row, c!=col]):
                cell_count += count_region_cell(matrix,r,c)
    return cell_count

if __name__ == '__main__':

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = find_max_region(matrix)

    print(result)
