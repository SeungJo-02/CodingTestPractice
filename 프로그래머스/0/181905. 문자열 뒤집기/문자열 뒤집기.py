def solution(my_string, s, e):
    answer = ''
    start = my_string[:s]
    end = my_string[e+1:]
    swich = my_string[s:e+1:][::-1]
    
    return start + swich + end