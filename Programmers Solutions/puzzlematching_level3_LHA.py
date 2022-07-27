def rotate(table):
    return list(map(list,zip(*table[::-1])))

def dfs(condition, table, key, value, visited):
    i, j, x, y, target = condition
    visited[i][j] = 1
    key.append((i,j))
    value.append((x,y))
    moves = [(-1,0), (1,0), (0,1), (0,-1)]
    for move in moves:
        dx, dy = move
        move_x, move_y = i + dx, j + dy
        if move_x < 0 or move_y < 0 or move_x >= len(table) or move_y >= len(table):
            continue
        elif table[move_x][move_y] == target and visited[move_x][move_y] == 0:
            key, value, visited = dfs([move_x, move_y, x+dx, y+dy, target], table, key, value, visited)
    return key, value, visited

def puzzle(table, target):
    visited = [[0]*len(table) for _ in range(len(table))]
    pieces = {} if target == 1 else []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == target and visited[i][j] == 0:
                key, value, v = dfs([i,j,0,0,target],table,[],[],visited)
                if target == 1:
                    pieces[tuple(key)] = value
                else:
                    pieces.append(value)
                visited = v
    return pieces

def solution(game_board, table):
    answer = 0
    board = puzzle(game_board,0)
    for _ in range(4):
        table = rotate(table)
        pieces = puzzle(table,1)
        for key,value in pieces.items():
            if value in board:
                board.remove(value)
                answer += len(value)
                for cod in key:
                    i, j  = cod
                    table[i][j] = 0
    return answer