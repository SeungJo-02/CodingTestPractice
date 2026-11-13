def solution(sizes):
    row = []
    col = []
    for i, j in sizes:
        if i >=j:
            row.append(i)
            col.append(j)
        else:
            row.append(j)
            col.append(i)
    return max(row)* max(col)
    