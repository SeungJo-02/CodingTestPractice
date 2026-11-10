import math
def solution(n, m):
    #최대공약수 gcd
    gcd = math.gcd(n,m)
    #최소공배수 lcm
    lcm = math.lcm(n,m)
    return [gcd, lcm]