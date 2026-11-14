def solution(n):
    front, back = 0, 1 # front f0, back f1
    for i in range(n): # 0이거나 1이면 어차피 1번 루프 
        front, back = back, (front + back)
    return front %1234567