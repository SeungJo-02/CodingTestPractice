def solution(X, Y):
    answer = []
    for i in range(9,-1,-1):
        word = str(i)
        Count_X = X.count(word)
        Count_Y = Y.count(word)
        
        answer.append(word * min(Count_X, Count_Y))
    result = "".join(answer)
    
    if result == "":
        return "-1"
    if result[0] == "0":
        return "0"
            
    return result