import os

def findMedian(n, arr):
    return sorted(arr)[n//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()