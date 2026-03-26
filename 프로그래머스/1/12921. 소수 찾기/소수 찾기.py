def solution(n):
    check = [True] * (n + 1)
    check[0] = False
    check[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if check[i]:
            for j in range(i*i, n+1,i):
                check[j] = False
    return check.count(True)