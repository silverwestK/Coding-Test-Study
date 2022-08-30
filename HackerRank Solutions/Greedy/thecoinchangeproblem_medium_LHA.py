#!/bin/python3

def getWays(n, c):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in c:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]

    return dp[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
