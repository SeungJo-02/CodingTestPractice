#인접행렬
INF = 999999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

#인접 리스트
graph1 = [[] for _ in range(3)] # row가 3개인 2차원 인접 리스트 표현

#(노드, 거리)
#노드 0
graph1[0].append((1,7))
graph1[0].append((2,5))
#노드 1
graph1[1].append((0,7))
#노드 2
graph1[2].append((0,5))
print(graph1)