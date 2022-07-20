#!/bin/python3

import os
import sys



def jeanisRoute(k, roads, cities):
    from collections import defaultdict
    sys.setrecursionlimit(10**7)
    g, start, cities = defaultdict(dict), cities[0], set(cities)
    for i,j, w in roads:
        g[i][j] = g[j][i] = w
    print('graph',g)
    visited = set()
    def dfs(node, dis=0):
        print('node',node,'dis',dis)
        visited.add(node)
        isBelong = node in cities
        print(isBelong)
        minus = [0,0]
        print('itmes',g[node].items())
        print('visited',visited)
        for i, val in g[node].items():
            if i not in visited:
                d = dfs(i, dis+val) - dis
                print('node',node,'d',d)
                if d > 0:
                    isBelong = True
                    ans[0] += 2 * g[node][i]
                    print('minus',minus)
                    if d > minus[0]:
                        minus[1], minus[0] = max(minus), d
                    else: minus[1] = max(minus[1], d)
        ans[1] = max(ans[1], sum(minus))
        print('return',dis + max(minus) if isBelong else 0)
        return dis + max(minus) if isBelong else 0
    ans = [0, 0]
    dfs(start)
    print('final ans',ans)
    return ans[0] - ans[1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    city = list(map(int, input().rstrip().split()))

    roads = []

    for _ in range(n-1):
        roads.append(list(map(int, input().rstrip().split())))

    result = jeanisRoute(k, roads, city)

    fptr.write(str(result) + '\n')

    fptr.close()
