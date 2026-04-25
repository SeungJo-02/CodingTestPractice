#입력값
n, m, k = map(int, input().split())
lists = list(map(int, input().split()))

lists.sort()

fir = lists[-1]
sec = lists[-2]

#가장 큰수의 횟수
count = m // (k + 1) * k
count += m % (k + 1)

result = 0

result += count * fir
result += m // (k + 1) * sec

print(result)