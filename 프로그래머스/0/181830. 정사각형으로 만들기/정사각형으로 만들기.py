def solution(arr):
    answer = [[]]
    row, column = len(arr), len(arr[0])
    
    if row < column:
        for i in range(column-row):
            arr.append([0] * (column))
            
    elif row > column:
        for i in range(row):
            arr[i] += [0] * (row - column) 
            
    else: 
        return arr
    return arr
