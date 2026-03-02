def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        i = int(i[s : s+l])
        if int(i) > k :
           answer.append(i)

    return answer