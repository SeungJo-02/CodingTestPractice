#연속된 숫자들의 합 -> 투 포인터(슬라이딩 윈도우) 사용하기
def solution(n):
    window_sum = 0 #현재 창 값
    num_minus = 1 # 1부터 하나하나 커지는 값이고 뺄 숫자다
    result = 0 #결과 
    
    for i in range(1, n + 1): # 1부터 전체 숫자를 창에 넣기
        window_sum += i 
        
        #다 더한 값이 전체보다 크면 하나씩 빼기
        while window_sum > n: # 작으면 패스(e.g. 1>15)
            window_sum -= num_minus
            num_minus += 1 #1부터 하나하나 커진 거를 빼야하니까
        # window_sum이 목표 숫자랑 같으면 결과 +1
        if window_sum == n:
            result +=1
    
    return result