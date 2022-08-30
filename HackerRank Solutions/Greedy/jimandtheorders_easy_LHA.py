#!/bin/python3
import os

def jimOrders(orders):
    orders = [[i + 1, t[0] + t[1]] for i, t in enumerate(orders)]
    orders.sort(key=lambda x: (x[1], x[0]))

    return list(zip(*orders))[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
