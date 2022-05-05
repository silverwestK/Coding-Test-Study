import os

def countingSort(arr):
    cntList = [0]*(max(arr)+1)
    for i in arr:
        cntList[i] += 1
    for i in range(1,len(cntList)):
        cntList[i] += cntList[i-1]

    result = [0]*len(arr)
    for i in arr:
        result[cntList[i]-1] = i
        cntList[i] -= 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
