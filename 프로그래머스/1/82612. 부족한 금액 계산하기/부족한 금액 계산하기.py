def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price + i * price
    if money < total:
        return total - money
    else:
        return 0

