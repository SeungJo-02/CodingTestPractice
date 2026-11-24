def solution(n, words):
    already = set()#이미 나온 단어
    
    #words 수 만큼 반복하기
    for i in range(len(words)):
        person_idx = (i % n) + 1 #사람 번호
        order_idx = (i // n) + 1 #자신이 몇 번째 차례인지 
        
    #이미 나온 단어이거나 끝말잇기가 안되면 탈락
        if (i>0 and words[i][0] != words[i-1][-1]) or words[i] in already:
            return [person_idx,order_idx]
        already.add(words[i])
            
    return [0,0]