def solution(absolutes, signs):
    return sum(i if b else -i for i, b in zip(absolutes, signs))