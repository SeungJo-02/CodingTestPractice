def solution(n, m, section):
    lastpainted = 0
    result = 0
    
    for num in section:
        if lastpainted < num:
            result += 1
            lastpainted = num + m -1
            
    return result