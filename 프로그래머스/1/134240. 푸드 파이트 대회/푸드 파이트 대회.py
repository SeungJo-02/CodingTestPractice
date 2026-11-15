def solution(food):
    answer = ''
    #음식 주문한 걸 넣고 거기서 2로 나눴을 때 몫 만큼 추가하기
    for i,v in enumerate(food):
        if (v // 2) != 0:
            mok = v//2
            for j in range(mok):
                answer += str(i)
    return answer + "0" + answer[::-1]