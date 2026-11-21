def solution(n):
    battery = 0
    #n이 0이 되면 Stop
    while n != 0:
        # 짝수면 n 만 줄이기
        if n % 2 == 0:
            n = n//2
        #홀수면 짝수로 만들어주고 배터리 하나 올리기
        else:
            n -= 1
            battery +=1
    
    return battery