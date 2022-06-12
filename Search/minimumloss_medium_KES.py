import os
import sys

def minimumLoss(price):
    idxWprice = [(i, v) for i, v in enumerate(price)]
    idxWprice.sort(key = lambda x:x[1])
    minVal = sys.maxsize
    for i in range(1, len(price)):
        if idxWprice[i][0] < idxWprice[i-1][0]:
            diff = idxWprice[i][1] - idxWprice[i-1][1]
            minVal = min(diff, minVal)
    return minVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
