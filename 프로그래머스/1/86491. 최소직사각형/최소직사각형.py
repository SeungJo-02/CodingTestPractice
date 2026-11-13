def solution(sizes):
    max_row = 0 #가로최대
    max_col = 0 #세로최대
    
    for r,c in sizes:
        max_row = max(max_row, max(r,c)) # 가장 큰 거만 
        max_col = max(max_col, min(r,c)) # 작은 거 중에 가장 큰 거
    return max_row * max_col