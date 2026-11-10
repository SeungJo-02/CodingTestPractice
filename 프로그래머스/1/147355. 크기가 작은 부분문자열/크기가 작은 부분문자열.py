def solution(t, p):
    answer = []
    for i in range(len(t)- len(p) + 1):
        answer.append(t[i:i + len(p)])
        
    return len([i for i in answer if i<= p])