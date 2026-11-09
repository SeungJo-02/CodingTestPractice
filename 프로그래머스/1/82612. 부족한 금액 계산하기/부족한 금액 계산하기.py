def solution(price, money, count):
    want = price * (count * (count +1) //2)

    return max(0, want - money)