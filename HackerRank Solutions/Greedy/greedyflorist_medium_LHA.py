#!/bin/python3
import os

def getMinimumCost(k, c):
    c.sort(reverse=True)
    q, r = divmod(n, k)

    total = 0
    for i in range(q + 1):
        total += sum(c[k * i:k * (i + 1)]) * (1 + i)

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
