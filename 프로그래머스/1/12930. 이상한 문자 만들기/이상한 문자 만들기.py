def solution(s):
    result = []
    #각각의 단어를 i에다가 넣기
    for i in s.split(" "):
        answer = ""
        for j in range(len(i)): #한 단어의 길이 만큼 반복
            if j % 2 == 0:# 짝수라면
                answer += i[j].upper() # 대문자로 바꾸고 추가하기
            else:
                answer += i[j].lower()
                
        result.append(answer)
                
    return " ".join(result)