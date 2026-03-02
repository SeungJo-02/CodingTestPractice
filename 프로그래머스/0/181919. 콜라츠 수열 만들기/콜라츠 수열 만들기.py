def solution(n):
    answer = []
    answer.append(n)
    while(True):
        if n == 1 :
            break
        elif n % 2 == 0:
            n /= 2 
            answer.append(n)
        else:
            n = n * 3 + 1
            answer.append(n)

    return answer