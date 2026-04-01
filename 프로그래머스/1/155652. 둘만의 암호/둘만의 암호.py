def solution(s, skip, index):
    alpha = [i for i in "abcdefghijklmnopqrstuvwxyz" if i not in skip]
    length = len(alpha)
    
    answer = ""
    
    for k in s:
        present = alpha.index(k)
        
        new = (present + index) % length
        
        answer += alpha[new]
    
    
    return answer