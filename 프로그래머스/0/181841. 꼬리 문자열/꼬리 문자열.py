def solution(str_list, ex):
    li = [i for i in str_list if ex not in i]
            
    return "".join(li)