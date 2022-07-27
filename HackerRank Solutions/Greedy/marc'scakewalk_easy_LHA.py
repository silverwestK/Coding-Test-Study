#!/bin/python3
import os

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    return sum([2 ** i * c for i, c in enumerate(calorie)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
