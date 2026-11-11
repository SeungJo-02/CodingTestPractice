def solution(s):
    count_zero = 0
    count_loop = 0
    while s != "1": #s가 1이 되면 탈출
        ones = s.count("1") # 1의 개수 세기랑 0 제거후 길이랑 같다
        count_zero += len(s) - ones #0 개수는 전체에서 1뺀거랑 같다
        
        s = f'{ones:b}' #길이의 이진법사용시 나오는 이진 숫자 
        count_loop += 1
        
    return [count_loop,count_zero]