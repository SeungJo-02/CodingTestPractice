def solution(myString, pat):
    answer = 0
    myString = myString.replace("A","X").replace("B","A").replace("X","B")
    if pat in myString : 
        answer = 1
    return answer