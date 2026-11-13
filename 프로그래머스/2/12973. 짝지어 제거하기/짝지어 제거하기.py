def solution(s):
    stack = [s[0]] # 스택에 하나 추가하기
    for i in range(1,len(s)): # 스택에 하나 추가했으니까
        if not stack:
            stack.append(s[i])
        
        elif stack[-1] != s[i]: #전알파벳이랑 지금 넣을 알파벳이 다르면
            stack.append(s[i])
        else:
            stack.pop()
            
    return 1 if not stack else 0