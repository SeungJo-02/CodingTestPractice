def solution(name, yearning, photo):
    result = []
    dic ={}
    for num in range(len(name)):
        dic[name[num]] = yearning[num]
    
    for time in photo:
        num = 0
        for names in time:
            if names in name:
                num += dic[names]
        result.append(num)
        
    return result