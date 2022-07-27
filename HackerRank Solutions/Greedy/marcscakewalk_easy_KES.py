import os

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = 0
    for i in range(len(calorie)):
        miles += 2**i * calorie[i]
    return miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
