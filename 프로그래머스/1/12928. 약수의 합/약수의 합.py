def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1): #제곱근 만큼 덜 반복하기
        if n % i == 0: # n의 약수라면
            answer += i #answer에 추가하기
            if i != n//i: # 짝수 약수인데 중복이라면(참/거짓)
                answer += n//i # 짝수 약수만 더하기
    return answer