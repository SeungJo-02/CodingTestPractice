def solution(k, score):
    answer = []
    li = []
    
    for s in score:
        answer.append(s)
        answer.sort(reverse = True)
        
        if len(answer) > k:
            answer.pop()
        
        li.append(answer[-1])
    return li