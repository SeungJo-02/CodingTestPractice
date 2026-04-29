n = int(input())

x , y = 1, 1

plans = input().split()

commends = ["L","R","U","D"]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in plans:
    nx = x
    ny = y
    for k in range(len(commends)):
        if i == commends[k]:
            nx = x + dx[k]
            ny = y + dy[k]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x,y)    