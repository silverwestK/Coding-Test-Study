import os

def candies(n, arr):
    candieState = [1] * n
    for i in range(n - 1):
        if arr[i] < arr[i + 1] and candieState[i] >= candieState[i + 1]:
            candieState[i + 1] = candieState[i] + 1
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1] and candieState[i] >= candieState[i - 1]:
            candieState[i - 1] = candieState[i] + 1

    return sum(candieState)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
