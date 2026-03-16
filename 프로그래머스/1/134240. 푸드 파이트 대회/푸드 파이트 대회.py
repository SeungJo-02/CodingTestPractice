def solution(food):
    answer = ''
    order = []
    for j in food:
        order.append(j//2)
    for i,v in enumerate(order):
        answer += str(i) * v
    right = answer[::-1]
    
    return answer + "0" + right