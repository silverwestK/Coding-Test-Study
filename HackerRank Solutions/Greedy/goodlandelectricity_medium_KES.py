import os
def pylons(k, arr):
    answer = 0
    i = 0
    plant = i+k-1
    while i < n:
        if arr[plant] == 1:
            i = plant+k
            plant = i+k-1
            answer += 1
            if plant >= n:
                plant = n-1
        else:
            plant -= 1
            if plant < i-k+1 or plant < 0:
                return -1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
