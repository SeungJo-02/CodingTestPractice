def solution(arr, divisor):
    answer = []
    for v in arr:
        if v % divisor == 0:
            answer.append(v)
    if len(answer)==0:
        return [-1]
    return sorted(answer)