from collections import deque

# 탈출 좌표
n, m = map(int, input().split())

#미로
graph = [ list(map(int, input())) for _ in range(n)]

#이동할 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]
            #못가는 곳 1
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #못가는 곳 2
            if graph[nx][ny] == 0:
                continue
            # 처음가는 곳 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))