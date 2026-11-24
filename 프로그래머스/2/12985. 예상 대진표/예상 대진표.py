def solution(n,a,b):
    answer = 0
    # a,b가 n 보다 큰 수면 안된다
    if a>n or b>n:
        return "err"
    #a랑 b가 만나게 되는 순간은 서로 숫자
    while a != b:
        # 짝수든 홀수든 (x+1)//2 하면 같은 숫자그룹이 된다
        a = (a+1)//2
        b = (b+1)//2
        answer +=1
    return answer