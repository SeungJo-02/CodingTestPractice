def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    r,c = 0,0
    posi = 0
    
    for i in range(1, n**2 + 1):
        answer[r][c] = i
        
        nr = r + dr[posi]
        nc = c + dc[posi]
        
        if nr < 0 or nr >= n or nc < 0 or nc >= n or answer[nr][nc] != 0:
            posi = (posi + 1)%4
            nr = r + dr[posi]
            nc = c + dc[posi]
        r, c = nr, nc
    return answer