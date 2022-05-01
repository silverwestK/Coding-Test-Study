#!/bin/python3
import os

def commonChild(s1, s2):
    inter_letter = set(s1).intersection(set(s2))
    if len(inter_letter)==0:
        return 0
    str1 = ''.join([c for c in s1 if c in inter_letter])
    str2 = ''.join([c for c in s2 if c in inter_letter])

    m = len(str1)
    n = len(str2)

    C = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1) :
        for j in range(n+1) :
            if i==0 or j==0 :
                C[i][j] = 0
            elif str1[i-1] == str2[j-1] :
                C[i][j] = C[i-1][j-1]+1
            else :
                C[i][j] = max(C[i-1][j], C[i][j-1])

    return C[m][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
