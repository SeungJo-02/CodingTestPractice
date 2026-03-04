def solution(myString):
    answer = []
    change = myString.split("x")
    for i in range(len(change)):
        answer.append(len(change[i]))
    return answer