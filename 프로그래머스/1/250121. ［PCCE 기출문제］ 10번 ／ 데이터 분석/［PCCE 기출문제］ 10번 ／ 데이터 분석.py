def solution(data, ext, val_ext, sort_by):
    info = {"code" : 0 , "date" : 1, "maximum" : 2, "remain" : 3}
    ext_idx = info[ext]
    sort_idx = info[sort_by]
    
    fillered_data = [ i for i in data if i[ext_idx] < val_ext]
    
    fillered_data.sort(key = lambda x : x[sort_idx])
    
    return fillered_data