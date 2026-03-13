def solution(t, p):
    answer = 0
    length = len(p)
    li = [t[i:i+length] for i in range(len(t)-length+1)]
    
    for k in li:
        if int(k) <= int(p):
            answer +=1
    return answer
