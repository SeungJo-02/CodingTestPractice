#퀵 정렬
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start # 기준
    left = pivot + 1 # 큰 수 찾기 위한 인덱스
    right = end      # 작은 수 찾기 위한 인덱스
    #오른쪽이 왼쪽보다 커지는 경우가 역전되는 상황까지 반복
    while left <= right: # 이거의 반대의 케이스는 다 훌터 봤다는 소리
        #피봇보다 작으면 패스(큰 수 찾기)
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피봇보다 크면 패스(작은 수 찾기)
        while right > start and array[right] >= array[pivot]:
            right -= 1
        #엇갈렸다면 피봇이랑 작은 수랑 교체
        if left>right:
            array[right], array[pivot] = array[pivot], array[right]
        # 아니라면 큰 수랑 작은 수랑 교채
        else:
            array[left], array[right] = array[right], array[left]
    #왼쪽 그룹과 오른쪽 그룹
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1 , end)

quick_sort(array,0, len(array)-1)
print(array)