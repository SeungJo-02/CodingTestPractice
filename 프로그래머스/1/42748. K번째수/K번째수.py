def solution(array, commands):
    answer = []
    for q in commands:
        i, j , k = q[0], q[1], q[2]
        li = array[i-1:j]
        li.sort()
        answer.append(li[k-1])
    return answer