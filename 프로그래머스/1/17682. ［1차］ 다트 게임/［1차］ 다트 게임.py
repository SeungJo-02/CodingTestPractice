def solution(dartResult):
    stack = []
    
    dartResult = dartResult.replace("10","k")
    
    for i in dartResult:
        if i.isdigit() or i == "k":
            stack.append(10 if i == "k" else int(i))
            
        elif i in ['S', 'D', 'T']:
            num = stack.pop()
            if i == "S" : stack.append(num ** 1)
            elif i == "D" : stack.append(num ** 2)
            elif i == "T" : stack.append(num ** 3)
            
        elif i == "*":
            score = stack.pop()
            if stack:
                pre = stack.pop()
                stack.append(pre *2)
            stack.append(score * 2)
            
        elif i == "#":
            score = stack.pop()
            stack.append(score * -1)
            
    return sum(stack)