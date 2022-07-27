def rotate(tables, d):
    N = len(tables)
    M = len(tables[0])
    # 90회전
    if d == 1:
        ret = [[0] * N for _ in range(M)]
        for r in range(N):
            for c in range(M):
                ret[c][N - 1 - r] = tables[r][c]
        return ret
    # 180회전
    elif d == 2:
        ret = [[0] * M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                ret[N - 1 - r][M - 1 - c] = tables[r][c]
        return ret
    # 270회전
    elif d == 3:
        ret = [[0] * N for _ in range(M)]
        for r in range(N):
            for c in range(M):
                ret[M - 1 - c][r] = tables[r][c]
        return ret


def find_puzzle(puzzle_board, start_x, start_y, p_type):
    from collections import deque
    min_x, min_y = 100, 100
    max_x, max_y = -1, -1
    # 좌우상하로 인접해있는 것들이 같은 퍼즐 조각이라고 할 수 있음
    possible_route = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    n = len(puzzle_board)
    q = deque()
    q.append([start_x, start_y])
    puzzles = []
    if p_type == 0:
        check = 1
    else:
        check = 0
    puzzle_board[start_x][start_y] = abs(check - 1)
    while q:
        cur = q.popleft()
        # 네모를 만들기 위해 최소, 최대값 찾음
        if cur[0] < min_x:
            min_x = cur[0]
        if cur[1] < min_y:
            min_y = cur[1]
        if cur[0] > max_x:
            max_x = cur[0]
        if cur[1] > max_y:
            max_y = cur[1]
        puzzles.append([cur[0], cur[1]])
        for i in possible_route:
            x = cur[0] + i[0]
            y = cur[1] + i[1]
            if x >= 0 and y >= 0 and x < n and y < n and puzzle_board[x][y] == check:
                puzzle_board[x][y] = abs(check - 1)
                q.append([x, y])
    if check == 1:
        rotate_puzzles = []
        puzzle_list = [[0] * ((max_y - min_y) + 1) for i in range((max_x - min_x) + 1)]
        for i in puzzles:
            puzzle_list[i[0] - min_x][i[1] - min_y] = 1
        puzzle_90 = rotate(puzzle_list, 1)
        puzzle_180 = rotate(puzzle_list, 2)
        puzzle_270 = rotate(puzzle_list, 3)
        rotate_puzzles.append(puzzle_list)
        rotate_puzzles.append(puzzle_90)
        rotate_puzzles.append(puzzle_180)
        rotate_puzzles.append(puzzle_270)
        return rotate_puzzles
    else:
        puzzle_list = [[0] * ((max_y - min_y) + 1) for i in range((max_x - min_x) + 1)]
        for i in puzzles:
            puzzle_list[i[0] - min_x][i[1] - min_y] = 1
        return puzzle_list
    return puzzles


def solution(game_board, table):
    import numpy as np
    answer = 0
    # 넣어야 할 퍼즐들
    table_puzzles = []
    # 채워질 수 있는 퍼즐 칸들
    empty_puzzle_board = []
    n = len(game_board)
    # 퍼즐 뽑아내기
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                table_puzzles.append(find_puzzle(table, i, j, 0))
            if game_board[i][j] == 0:
                empty_puzzle_board.append(find_puzzle(game_board, i, j, 1))

    # 뽑아낸 퍼즐로 돌려보기
    for i in empty_puzzle_board:
        for j in range(len(table_puzzles)):
            if i in table_puzzles[j]:
                del table_puzzles[j]
                pu = np.array(i)
                answer = answer + int(pu.sum())
                break
    return answer