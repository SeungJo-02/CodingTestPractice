def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0,0,0]
    
    for i, answer in enumerate(answers):
        if p1[i % len(p1)] == answer:
            scores[0] += 1
            
        if p2[i % len(p2)] == answer:
            scores[1] += 1
            
        if p3[i % len(p3)] == answer:
            scores[2] += 1
            
    max_score = max(scores)
    
    result = []
    
    for i, v in enumerate(scores):
        if max_score == v:
            result.append(i + 1)
            
    return result