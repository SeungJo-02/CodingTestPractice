n,k = map(int, input().split()) 
result = 0

while True:
    rest = n % k 
    result += rest 
    n -= rest 
    if n < k:
        break
    result += 1
    n //= k 

result += (n - 1)

print(result)