def solution(want, number, discount):
    # 10일 안에 원하는 상품만큼 상품이 있어야한다
    # 답으로 쓸 숫자
    choice_day = 0
    #리스트
    dic = dict(zip(want, number))
    
    # 반복은 discount 개수 -9 만큼 반복 
    for s in range(len(discount)-9):
        dic2 ={}
        li = discount[s:s+10] #범위는 10개씩
        #dic2에 없으면 1추가 있으면 +1
        for i in li:
            dic2[i] = dic2.get(i, 0) + 1
        # 같으면 추가
        if dic == dic2:
            choice_day +=1
                
    return choice_day