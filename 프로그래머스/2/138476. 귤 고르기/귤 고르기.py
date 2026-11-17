from collections import Counter
def solution(k, tangerine):
    result = 0
    total = 0
    #귤 종류 몇 개 있는가
    counts = sorted(Counter(tangerine).values(), reverse = True)
    
    # k랑 result랑 같아지면 멈추기
    for i in counts:
        total += i #현재 크기의 귤 개수만큼 상자에 추가
        result +=1 #귤 종류 추가
        if total >= k: # 목표 만큼 채웠으면 종료
            break
    
    return result