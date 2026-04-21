#n : 데이터 개수 ,m : 반복 수 , k : 최소 반복
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
#가장 큰 수랑 그 다음 큰 수
first = data[-1]
second = data[-2]

#결과입력
result = 0

#반복
while True:
    for i in range(k): #가장 큰 수 최고 반복
        if m == 0:
            break
        result += first
        m -=1
    if m == 0:
        break
    result += second
    m-=1

print(result)




