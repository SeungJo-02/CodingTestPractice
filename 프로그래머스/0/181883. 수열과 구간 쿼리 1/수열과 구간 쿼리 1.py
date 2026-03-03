def solution(arr, queries):
    for i, v in enumerate(queries):
        s = v[0]
        e = v[1]
        for i in range(s,e+1):
            arr[i] +=1
        
        
    return arr