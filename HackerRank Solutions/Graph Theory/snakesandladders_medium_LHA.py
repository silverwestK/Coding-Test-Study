#!/bin/python3
import os
from collections import deque


def quickestWayUp(ladders, snakes):
    all_paths = dict(ladders + snakes)
    que = deque([(0, 1)])
    visited = set()
    visited.add(1)

    while que:
        rolls, cur_pos = que.popleft()
        if cur_pos >= 100:
            return rolls

        for i in range(1, 7):
            nxt = cur_pos + i
            if nxt in all_paths:
                next_pos = all_paths[nxt]
            else:
                next_pos = nxt
            if next_pos not in visited:
                visited.add(next_pos)
                que.append((rolls + 1, next_pos))

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
