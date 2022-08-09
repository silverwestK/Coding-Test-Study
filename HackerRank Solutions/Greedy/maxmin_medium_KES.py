import os

def maxMin(k, arr):
    arr.sort()
    minUF = arr[k - 1] - arr[0]
    for i in range(1, len(arr) - k + 1):
        minUF = min(minUF, arr[i + k - 1] - arr[i])
    return minUF

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
