def solution(n, arr1, arr2):
    answer = []
    for j in range(n):
        bin_row = bin(arr1[j] | arr2[j])[2:].zfill(n)
        row = bin_row.replace("1","#").replace("0"," ")
        answer.append(row)
    return answer