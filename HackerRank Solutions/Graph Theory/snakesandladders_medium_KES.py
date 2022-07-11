from collections import deque
import os

def quickestWayUp(ladders, snakes):
    moveUpDown = ladders + snakes
    board = {}
    for f, t in moveUpDown:
        board[f] = t

    visited = [True] * 101
    queue = deque([(1, 0)])
    while queue:
        tempPos, rollCnt = queue.popleft()
        if tempPos >= 100:
            return rollCnt

        visited[tempPos] = False
        for i in range(1, 7):
            movedPos = tempPos + i
            if movedPos <= 100 and visited[movedPos]:
                if movedPos in board:
                    queue.append((board[movedPos], rollCnt + 1))
                else:
                    queue.append((movedPos, rollCnt + 1))
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
