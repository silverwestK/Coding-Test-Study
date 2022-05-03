import os

def runningTime(n, arr):
    cnt = 0
    for end in range(1, n):
        target = arr[end]
        i = end
        while i > 0 and arr[i-1] > target:
            arr[i] = arr[i-1]
            i, cnt = i-1, cnt+1
        arr[i] = target
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
