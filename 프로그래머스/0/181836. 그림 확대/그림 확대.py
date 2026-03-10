def solution(picture, k):
    answer = []
    for i in picture:
        row = "".join([j * k for j in i])
    
        for _ in range(k):
            answer.append(row)
    return answer