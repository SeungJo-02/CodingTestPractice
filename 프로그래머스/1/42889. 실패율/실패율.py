def solution(N, stages):
    answer = {}
    total_players = len(stages)
    
    for stage in range(1, N + 1):
        if total_players > 0:
            count = stages.count(stage)
            fail_rate = count/total_players
            answer[stage] = fail_rate
            total_players -= count 
            
            
        else:
            answer[stage] = 0
    
    
    
    
    
    
    
    return sorted(answer, key=lambda x : answer[x], reverse = True)