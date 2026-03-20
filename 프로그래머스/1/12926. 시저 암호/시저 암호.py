def solution(s, n):
    answer = ''
    for i in s:
        num = 0
        if i.isupper():
            num = (ord(i) - ord("A") + n) % 26 + ord("A")
            answer += chr(num)
        elif i.islower():
            num = (ord(i) - ord("a") + n) % 26 + ord("a")
            answer += chr(num)
        else:
            answer += " "
            
    return answer