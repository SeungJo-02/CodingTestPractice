def solution(arr, flag):
    answer = []
    for i,v in enumerate(flag):
        if v : #T/F
            for k in range(arr[i]*2):
                answer.append(arr[i])
        else:
            answer = answer[:-arr[i]]
    return answer