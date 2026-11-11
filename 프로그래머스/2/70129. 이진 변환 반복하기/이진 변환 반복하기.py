def solution(s):
    count_zero = 0
    count_loop = 0
    while s != "1": #s가 1이 되면 탈출
        count_zero += s.count("0") # 0세기
        s = bin(s.count("1"))[2:] #1의 개수와 남은 길이의 개수가 같음
        count_loop +=1
        
    return [count_loop,count_zero]