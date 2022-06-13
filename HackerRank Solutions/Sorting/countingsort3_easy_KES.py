import os

def countingSort(arr):
    result = [0] * 100
    for i in arr:
        result[i] += 1
    for i in range(1, len(result)):
        result[i] += result[i - 1]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []
    for _ in range(n):
        v, _ = input().strip().split()
        arr.append(int(v))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
