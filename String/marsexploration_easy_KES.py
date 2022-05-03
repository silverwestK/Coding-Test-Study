import os

def marsExploration(s):
    cnt = 0
    for i, c in enumerate(s):
        if ['S','O','S'][i%3] != c:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
