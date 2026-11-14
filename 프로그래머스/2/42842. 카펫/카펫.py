def solution(brown, yellow):
    #전체 합
    total = brown + yellow
    # 약수 쌍 모음
    pairlist = [[i,total//i] for i in range(1, total) if total % i == 0]
    # yellow는 전체 가로 및 세로 길이의 -2 씩이다.
    # 리스트에 있는 거 넣어서 yellow == 리스트 속 전체 길이 -2 한 거 를 곱한 거
    for ga, se in pairlist:
        if (ga-2) * (se-2) == yellow and ga >= se:
            return [ga,se]