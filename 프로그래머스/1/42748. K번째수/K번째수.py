def solution(array, commands):
    result = []
    
    #commands 수만큼 반복하기(리스트 당 3개의 원소를 가짐)
    #i:처음(-1 필요) , j:끝 , k:번째(-1 필요)
    for i,j,k in commands:
        result.append(sorted(array[i-1:j])[k-1])
    return result