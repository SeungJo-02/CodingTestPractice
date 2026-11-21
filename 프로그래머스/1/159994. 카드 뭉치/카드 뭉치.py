def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0
    #goal만큼 반복이고 요소 하나씩 비교
    for i in goal:
        # 만약 첫번째 카드랑 goal의 문자랑 같으면 카드사용
        # 그리고 카드를 다 썼는지 확인 
        if idx1 < len(cards1) and cards1[idx1] == i:
            idx1 += 1
        # 만약 2번째 카드랑 goal의 문자랑 같으면 카드사용
        # 그리고 카드를 다 썼는지 확인 
        elif idx2 < len(cards2) and cards2[idx2] == i:
            idx2 += 1
        else: 
            return "No"
    
    return "Yes"