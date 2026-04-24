# 시각문제 

#시간 입력 받기
h = int(input())

#전체 3의 개수 세기
count = 0
for i in range(h + 1): # 시 반복
    for j in range(60): # 분 반복
        for k in range(60): #초 반복
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)