#왕실 나이트 

#위치 입력
n = input()
# 행과 열 
row = int(n[1])
column = int(ord(n[0])) - int(ord("a")) + 1

steps =[(-2,-1),(-1,-2),(2,-1),(-1,2),(-2,1),(1,-2),(1,2),(2,1)]

count = 0

for step in steps:
    nrow = row + step[0]
    ncol = column + step[1]

    if nrow >=1 and nrow <=8 and ncol >=1 and ncol <=8:
        count += 1

print(count)