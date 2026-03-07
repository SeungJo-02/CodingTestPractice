def solution(arr, delete_list):
    for i,v in enumerate(delete_list):
        if v in arr:
            arr.remove(v)
    return arr