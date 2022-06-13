from collections import Counter, defaultdict
import os

factorialDict = {}
i_factorialDict = {}
cntDict = defaultdict(Counter)
m = 10 ** 9 + 7

def initialize(s):
    factorialDict[0], i_factorialDict[0], cntDict[0] = 1, 1, Counter(s[0])
    for i in range(1, len(s)):
        factorialDict[i] = (i * factorialDict[i - 1]) % m
        i_factorialDict[i] = pow(factorialDict[i], m - 2, m)
        cntDict[i] = cntDict[i - 1] + Counter(s[i])

def answerQuery(l, r):
    target = cntDict[r - 1] - cntDict[l - 2]
    evens, odds, fact = 0, 0, 1
    for v in target.values():
        if v >= 2:
            evens += v // 2
            fact *= i_factorialDict[v // 2]
        if v % 2 != 0:
            odds += 1
    return (max(1, odds) * factorialDict[evens] * fact) % m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
