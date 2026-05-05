import sys

sys.setrecursionlimit(10**6)

# n, m 입력
n, m = map(int, input().split())

#그래프 입력
graph = [ list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    # 범위 벗어나면 끝
    if x <= -1 or y <= -1 or x >= n or y >= m: 
        return False
    # 하나 선택한게 0이라면 주변에 있는거 모두 1로 바꾸기
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x -1, y)
        dfs(x +1, y)
        dfs(x , y + 1)
        dfs(x , y - 1)
        return True
    # 1이라면
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)