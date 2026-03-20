def solution(food):
    answer = ''
    order = []


    for i in food:
        order.append(i//2)

    for j,k in enumerate(order):
        answer += str(j) * k
    
    return answer+"0"+answer[::-1]