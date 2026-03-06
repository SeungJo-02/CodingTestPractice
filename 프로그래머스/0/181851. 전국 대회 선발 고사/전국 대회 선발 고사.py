def solution(rank, attendance):
    answer = 0
    attend = []
    for i, v in enumerate(attendance):
        if v :
            attend.append((rank[i],i))
    attend = sorted(attend)
    
    a = attend[0][1]
    b = attend[1][1]
    c = attend[2][1]
    
    
    return 10000*a + 100*b + c