#!/bin/python3
import os

def closestNumbers(arr):
    sorted_arr = sorted(arr)
    min_diff = [(0, abs(sorted_arr[1] - sorted_arr[0]))]

    for i in range(1, len(sorted_arr) - 1):
        diff = abs(sorted_arr[i + 1] - sorted_arr[i])
        if diff < min_diff[0][1]:
            min_diff = []
            min_diff.append((i, diff))
        elif diff == min_diff[0][1]:
            min_diff.append((i, diff))

    result = []
    for s in min_diff:
        result.append(sorted_arr[s[0]])
        result.append(sorted_arr[s[0] + 1])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
