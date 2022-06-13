import os

def theLoveLetterMystery(s):
    n = int(round(len(s)/2))
    res = 0
    for a, b in zip(s[:n], s[::-1][:n]):
        if a != b:
            res += abs(ord(a)-ord(b))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
