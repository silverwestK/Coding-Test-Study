#!/bin/python3
import os

def minimumLoss(price):

    min_loss = 10 ** 16
    years = {}
    for y, p in enumerate(price):
        years[p] = y

    price.sort()
    for i in range(len(price) - 1):
        if price[i + 1] - price[i] < min_loss and years[price[i + 1]] < years[price[i]]:
            min_loss = price[i + 1] - price[i]

    return min_loss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
