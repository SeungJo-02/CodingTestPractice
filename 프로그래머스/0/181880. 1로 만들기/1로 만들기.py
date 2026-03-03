def solution(num_list):
    answer = 0
    for i,v in enumerate(num_list):
        while(True):
            if v == 1:
                break
            elif v%2 == 0:
                v =  v // 2
                answer+=1
            elif v % 2 != 0:
                v =  (v - 1) // 2
                answer += 1
                    
    return answer