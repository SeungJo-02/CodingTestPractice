#n : 데이터 개수 ,m : 반복 수 , k : 최소 반복
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
#가장 큰 수랑 그 다음 큰 수
first = data[-1]
second = data[-2]

#수열의 길이 k + 1
#가장 큰 수의 개수 구하기 
count = m//(k + 1) * k + m % (k + 1) # 몫 * k 만큼 + 나머지 * K

result = 0
result += count * first #가장 큰 수 더하기
result += second * (m - count)# 다음 큰 수 더하기(몫 * 다음 큰 수)

print(result)
