def solution(price, money, count):
    want = 0
    for i in range(1, count + 1):
        want += price * i
        
    if money < want:
        return want - money 
    else:
        return 0