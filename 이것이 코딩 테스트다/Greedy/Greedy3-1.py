#n은 행 m은열
n,m = map(int, input().split())

result = 0

for card in range(n):#n행 만큼 반복
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(result, min_val)

print(result)