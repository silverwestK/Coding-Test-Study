#!/bin/python3
import os
from collections import Counter

def missingNumbers(arr, brr):
    cnt_a = Counter(arr)
    cnt_b = Counter(brr)

    missing = [k for k in cnt_b.keys()
               if (k not in cnt_a.keys() or cnt_a[k] != cnt_b[k])]

    return sorted(missing)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
