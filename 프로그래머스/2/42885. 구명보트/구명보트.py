#가장 가벼운 사람과 무거운 사람을 짝지어서 숫자 올리기
def solution(people, limit):
    people.sort()
    light = 0
    heavy = len(people) - 1
    answer = 0
    #둘이 합쳐서 
    while light <= heavy:
        if people[light]+people[heavy]<=limit:
            light +=1
            heavy -=1
            answer +=1
        else:
            heavy -=1
            answer +=1
    
    return answer