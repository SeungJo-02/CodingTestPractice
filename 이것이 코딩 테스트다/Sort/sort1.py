# 선택정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_dex = i
    for j in range(i + 1, len(array)):
        if array[min_dex] > array[j]:
                min_dex = j
    array[i], array[min_dex] = array[min_dex], array[i]