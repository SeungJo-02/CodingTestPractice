def solution(s):
    parsing = list(map(int, s.split()))
    Min, Max = min(parsing), max(parsing)
    return f"{Min} {Max}"