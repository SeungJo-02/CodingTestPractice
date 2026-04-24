# 상하좌우 문제

#공간의 크기 n 입력
n = int(input())
#이동 계획 입력
move = input().split()
#시작 위치 설정
x, y = 1 ,1

#L R U D 정의  
dx = [-1, 1 ,0 ,0]
dy = [0, 0, -1, 1]
commend = ["L","R","U","D"]

#로직
for i in move: #입력한 개수 만큼 반복
    for k in range(len(commend)): # 커멘드 인덱스 사용하기 위함 
        if i == commend[k]: # 커멘드 확인
            nx = x + dx[k]
            ny = y + dy[k]

    if nx < 1 or ny < 1 or nx > n or ny > n: # 예외 검즘
        continue

    x,y = nx, ny

print(x,y)