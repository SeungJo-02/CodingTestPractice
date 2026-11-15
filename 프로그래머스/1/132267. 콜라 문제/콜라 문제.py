def solution(a, b, n):
    result = 0
    new_coke = 0
    #n이 a보다 작으면 멈추기
    while n >= a:
        new_coke = (n//a) * b # 받게 되는 콜라
        result += new_coke
        n = new_coke + (n % a) # n 최신화
        
    return result