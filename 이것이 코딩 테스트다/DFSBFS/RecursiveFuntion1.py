def recursive_funtion(i):
    if i == 100:
        return
    print(i ,"재귀 함수에서", f"{i+1}번째 재귀 함수 호출")
    recursive_funtion(i+1)# 여기에서 다시 recursive_funtion(i)으로 넘어가니까 다시 print(i ,"재귀 함수에서", f"{i+1}번째 재귀 함수 호출")가 나옴
    print(f"{i}번째 재귀 함수 종료")

recursive_funtion(1)
# 즉 재귀함수는 스택 자료구조와 다르지 않다