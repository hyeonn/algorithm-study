from collections import deque

N, M = map(int, input().split())
graph = []

def bfs(x, y):
    # 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현 위치의 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위 지정
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽
            elif graph[nx][ny] == 0:
                continue
            # 이동할 수 있는 길
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]

for _ in range(N):
    graph.append(list(map(int, input())))

print(bfs(0, 0))