def solution(num_list):
    answer = 0
    even = sum(num_list[::2])
    odd = sum(num_list[1::2])
    if even > odd:
        answer = even
    else :
        answer = odd
    
    
    return answer