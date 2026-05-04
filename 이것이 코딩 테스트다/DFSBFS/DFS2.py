#DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True # 방문함
    print(v, end = ' ')# 방문한 노드 출력
    for i in graph[v]:# 이 노드에 이어진 다른 노드 
        if not visited[i]:# 그 노드가 방문하지 않았다면 
            dfs(graph,i,visited)# dfs 실행
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)
dfs(graph, 1, visited)