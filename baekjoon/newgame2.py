# 동 서 북 남
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

White = 0
Red = 1
Blue = 2

rev_direction = {0: 1, 1: 0, 2: 3, 3: 2}

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

marker = dict()
board_2 = {(i, j): [] for j in range(n) for i in range(n)}

for i in range(1, k + 1):
    x, y, d = map(int, input().split())
    marker[i] = [x - 1, y - 1, d - 1]
    board_2[(x - 1, y - 1)].append(i)

def solve():
    turn = 0
    P = 0
    while True:
        turn += 1
        if turn > 1000: return -1
        for num in range(1, k + 1):
            x, y, d = marker[num]
            nx, ny = x + dx[d], y + dy[d]
            # 맵을 벗어나는 경우 or 칸이 파란색인 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == Blue:
                nd = rev_direction[d]
                nx, ny = x + dx[nd], y + dy[nd]
                # 가만히 있는 경우 -> 방향만 바뀜
                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == Blue:
                    marker[num][2] = nd
                    continue
                P = 1
            # 흰색인 경우
            if board[nx][ny] == White:
                left = board_2[(x, y)][:board_2[(x, y)].index(num)]
                right = board_2[(x, y)][board_2[(x, y)].index(num):]
                board_2[(x, y)] = left
                board_2[(nx, ny)].extend(right)
                if len(board_2[(nx, ny)]) >= 4: return turn
                for i in right:
                    marker[i][0], marker[i][1] = nx, ny
                if P == 1: marker[num][2] = nd; P = 0
            # 빨간색인 경우
            elif board[nx][ny] == Red:
                left = board_2[(x, y)][:board_2[(x, y)].index(num)]
                right = board_2[(x, y)][board_2[(x, y)].index(num):]
                board_2[(x, y)] = left
                right.reverse()
                board_2[(nx, ny)].extend(right)
                if len(board_2[(nx, ny)]) >= 4: return turn
                for i in right:
                    marker[i][0], marker[i][1] = nx, ny
                if P == 1: marker[num][2] = nd; P = 0

print(solve())
