def solution(k, score):
    result = []
    honor = []
    for i in score:
        honor.append(i)
        honor.sort(reverse=True)
        if len(honor) > k:
            honor.pop()
        result.append(honor[-1])
    return result