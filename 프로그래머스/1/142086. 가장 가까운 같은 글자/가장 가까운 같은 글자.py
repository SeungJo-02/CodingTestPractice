def solution(s):
    answer = []
    dic = {}
    for i, v in enumerate(s):
        if v not in dic: #v(값)이 dic에 없으면 
            dic[v] = i # 인덱스 최신화
            answer.append(-1)
        else: #있으면
            answer.append(i-dic[v])
            dic[v] = i #인덱스 최신화 

    return answer