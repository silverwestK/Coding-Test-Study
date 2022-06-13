import os

def funnyString(s):
    res = [abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1)]
    return 'Funny' if res == res[::-1] else 'Not Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
