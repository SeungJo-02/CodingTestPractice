n,k = map(int, input().split())

count = 0

while n >= k:
    rest = n % k
    count += rest
    n -= rest

    n //= k
    count += 1

count += (n - 1)

print(count)