def solution(s):
    answer = 0
    same = 0 
    diff = 0
    top = ""
    for i in s:
        if top == "" :
            top = i
            same = 1
            diff = 0
            continue
        
        if top == i:
            same += 1
        else:
            diff += 1
            
        if same == diff:
            answer +=1
            same = 0
            diff = 0
            top = ""
       
    if top != "":
        answer += 1
    
    return answer