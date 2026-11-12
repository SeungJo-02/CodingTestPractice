def solution(n):
    jinsu_reverse = ""
    while n > 0:
        n, mod = divmod(n,3) # n에는 몫, mod에는 나머지
        jinsu_reverse += str(mod) #문자열로 
        
    return int(jinsu_reverse, 3)