def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        digi = set(str(i))

        if digi <= {"0","5"}:
            answer.append(i)

    return answer if answer else [-1]