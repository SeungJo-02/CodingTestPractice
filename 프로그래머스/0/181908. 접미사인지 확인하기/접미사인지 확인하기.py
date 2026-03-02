def solution(my_string, is_suffix):
    answer = 0
    jup = []
    for i in range(len(my_string)):
        jup.append(my_string[i:])
    if is_suffix in jup:
        return 1
    else :
        return answer