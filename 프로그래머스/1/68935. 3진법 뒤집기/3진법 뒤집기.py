def solution(n):
    answer = ""
    while(True):
        mok = n // 3
        rest = n % 3
        if mok !=0:
            answer += str(rest)
            n = mok
        else:
            answer += str(rest)
            break
    return int(answer,3)