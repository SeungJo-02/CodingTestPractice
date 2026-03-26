def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        skip = False
        for c in can:
            if c *2 in b:
                skip = True
                break
        if skip : continue
        
        for c in can:
            b = b.replace(c, " ")
        
        if b.strip() == "":
            answer += 1
            
    return answer