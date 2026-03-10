# 아 4500, 라 5000 상관없이
# 메뉴만 적으면 아이스 
# 아무거나 아아
def solution(order):

    return sum([5000 if 'latte' in i else 4500 for i in order])