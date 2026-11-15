def solution(s):
    # 먼저 노가다로 글짜 쪼개서 리스트로 만들기 
    words = "zero one two three four five six seven eight nine".split()
    #인덱스랑 값을 분리해서 반복문 돌리고 결과에 넣기
    for i ,v in enumerate(words):
        s = s.replace(v,str(i))
    return int(s)