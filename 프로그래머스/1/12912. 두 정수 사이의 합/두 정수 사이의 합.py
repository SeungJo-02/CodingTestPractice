def solution(a, b):
    answer = []
    for i in range(abs(a-b)+1):
        if a < b :
            answer.append(i+a)
        elif a > b:
            answer.append(i+b)
        else:
            return a
    return sum(answer)