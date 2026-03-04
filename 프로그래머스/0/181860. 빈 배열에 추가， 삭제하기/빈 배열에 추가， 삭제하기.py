def solution(arr, flag):
    answer = []
    for num, bol in zip(arr, flag):
        if bol:
            for i in range(num *2):
                answer.append(num)
        else: answer = answer[:-num]
    return answer