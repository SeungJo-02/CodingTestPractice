def solution(arr):
    stack = []
    for num in arr:
        if not stack or stack[-1] != num: #스택이 비거나 다음 숫자랑 안같으면 추가
            stack.append(num)
    return stack