import os

def closestNumbers(arr):
    arr = sorted(arr)
    mindiff, result = arr[1] - arr[0], []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff == mindiff:
            result.extend([arr[i - 1], arr[i]])
        elif diff < mindiff:
            mindiff = diff
            result = [arr[i - 1], arr[i]]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
