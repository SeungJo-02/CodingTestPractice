def solution(lottos, win_nums):
    
    count_zero = lottos.count(0)
    
    count_match = 0
    for i in lottos:
        if i in win_nums:
            count_match += 1
            
    rank = [6,6,5,4,3,2,1]
    
    bestRank = rank[count_match + count_zero]
    worstRank = rank[count_match]
    
    return [bestRank, worstRank]