dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def change(d, c):
    if (c == "L"):
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

def start():
    cnt = 0
    x,y = 0, 0
    arr[x][y] = 3
    d = 0
    idx = 0
    snake = []   # 뱀의 꼬리부터 머리까지 queue
    snake.append((0, 0))   # x, y
    while True:
        if board[idx][0] == cnt:     # 방향 전환
            d = change(d, board[idx][1])
            idx += 1
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위안에 있고, 자신이 아닌 경우
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 3:
            # 사과를 먹는 경우 -> 꼬리 그대로
            if arr[nx][ny] == 1:
                arr[nx][ny] = 3
                snake.append((nx, ny))
            # 사과를 못먹는 경우 -> 꼬리 하나 떼기
            elif arr[nx][ny] == 0:
                arr[nx][ny] = 3
                snake.append((nx, ny))
                tx, ty = snake.pop(0)
                arr[tx][ty] = 0
            x = nx
            y = ny
            cnt += 1
        else:
            cnt += 1
            break
    return cnt


n = int(input())
k = int(input())
arr = [[0] * n for i in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
l = int(input())
board = [[0, 0]] * 10000
for i in range(l):
    x, c = input().split()
    board[i] = [int(x), c]
print(start())