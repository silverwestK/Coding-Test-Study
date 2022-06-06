import os

def pairs(k, arr):
    arr.sort()
    cnt = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            diff = arr[j]-arr[i]
            if k == diff:
                cnt+=1
            elif k < diff:
                break
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
