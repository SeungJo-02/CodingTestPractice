def solution(order):
    answer = 0
    for i in order:
        if 'americano' in i:
            answer += 4500
        elif 'latte' in i :
            answer += 5000
        elif 'anything' in i:
            answer += 4500
            
    return answer



# 아 4500, 라 5000 상관없이
# 메뉴만 적으면 아이스 
#아무거나 아아