def solution(n):
    text = str(n)
    answer = sorted(text, reverse = True)
    
    return int("".join(answer))