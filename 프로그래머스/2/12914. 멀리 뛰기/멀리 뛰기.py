# 동적 계획법(DP)를 사용해서 푸는 문제다
def solution(n):
    if n ==1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    #3번째부터는 전값 전전값 더해야한다
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[-1] % 1234567