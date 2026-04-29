#맵 전체 크기 입력
import array

n,m = map(int, input().split())

#가보지 못한 위치 저장
save = [[0] * m for _ in range(n)]

#시작 위치랑 방행 입력
x,y,d = map(int, input().split())

#방문한 위치 처리
save[x][y] = 1

#전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

#시물레이션 시작
couunt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if save[nx][ny] == 0 and array[nx][ny] == 0:
        save[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    else:
        turn_time += 1
        if turn_time == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0
print(count)
