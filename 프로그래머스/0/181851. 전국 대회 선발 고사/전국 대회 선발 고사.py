def solution(rank, attendance):
    answer = 0
    attend = []
    result = []
    for i, v in enumerate(attendance):
        if v :
            attend.append(rank[i])
    attend = sorted(attend)
    
    for k in attend:
        result.append(rank.index(k))
    
    
    return 10000*result[0] + 100*result[1] + result[2]