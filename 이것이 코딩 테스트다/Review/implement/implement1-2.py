h = int(input())

count = 0
for hour in range(h+1):
    for time in range(60):
        for min in range(60):
            if "3" in str(hour)+str(time)+str(min):
                count += 1