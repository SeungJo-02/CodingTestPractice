def solution(s):
    s = list(map(int,s.split()))
    mini, maxi = str(min(s)), str(max(s))
    return mini + " " + maxi