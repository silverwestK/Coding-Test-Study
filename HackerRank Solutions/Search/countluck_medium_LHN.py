#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#


def check_out_of_bound(r, c, forest):
    return 0 > r or r >= len(forest) or 0 > c or c >= len(forest[0]) or forest[r][c] == 'X' or forest[r][c] == '1'


def is_splited_way(r, c, forest, ds):
    cnt = 0
    for d in ds:
        dr = r + d[0]
        dc = c + d[1]
        if (not check_out_of_bound(dr, dc, forest)) and (forest[dr][dc] == '.' or forest[dr][dc] == '*'):
            cnt += 1
            if cnt >= 2:
                return True
    return False


def find_portkey(r, c, forest):
    global rotate_count
    if check_out_of_bound(r, c, forest):
        return False

    if forest[r][c] == '*':
        return True

    ds = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    if is_splited_way(r, c, forest, ds):
        forest[r][c] = '1'
    else:
        forest[r][c] = 'X'

    for d in ds:
        dr = r + d[0]
        dc = c + d[1]

        if find_portkey(dr, dc, forest):
            if forest[r][c] == '1':
                rotate_count += 1
            return True

    return False


def countLuck(matrix, k):
    global rotate_count
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i])
        try:
            col = int(matrix[i].index('M'))
            row = i
        except:
            a = 1
    find_portkey(row, col, matrix)

    print('count', rotate_count)

    print("Impressed" if rotate_count == k else "Oops!")


if __name__ == '__main__':
    rotate_count = 0
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        forest = []

        for _ in range(n):
            matrix_item = input()
            forest.append(matrix_item)

        k = int(input().strip())

        countLuck(forest, k)



