def solution(s):
    answer = []
    
    for j in s.split(" "):
        temp = ""
        for i,v in enumerate(j):
            if i % 2 == 0:
                temp += v.upper()
            else:
                temp += v.lower()
        answer.append(temp)
    
    
    
    return " ".join(answer)