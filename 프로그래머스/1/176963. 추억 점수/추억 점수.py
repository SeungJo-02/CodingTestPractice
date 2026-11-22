def solution(name, yearning, photo):
    #이름과 점수를 매칭 dic으로
    name_scr = dict(zip(name, yearning))
    
    #photo 속 리스트 만큼 반복
    result = [sum(name_scr.get(person,0) for person in li) for li in photo]
        
    return result