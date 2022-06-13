import os

def balancedSums(n, arr):
    for i in range(1, n):
        arr[i] += arr[i - 1]
    if arr[0] == arr[-1]:
        return 'YES'
    for i in range(1, n):
        if arr[i - 1] == (arr[-1] - arr[i]):
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(n, arr)

        fptr.write(result + '\n')

    fptr.close()
