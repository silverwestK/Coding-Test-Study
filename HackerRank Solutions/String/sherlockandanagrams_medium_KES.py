from math import comb
import os

def sherlockAndAnagrams(s):
    cnt = 0
    for k in range(1,len(s)):
        tokens = {}
        for i in range(len(s)-k+1):
            try: tokens[''.join(sorted(s[i:i+k]))] += 1
            except: tokens[''.join(sorted(s[i:i+k]))] = 1
        for val in tokens.values():
            cnt += comb(val, 2)
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
