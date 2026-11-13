def solution(n):
    bin_n = bin(n)[2:] # n의 이진수 
    ones = bin_n.count("1") # n의 1의 개수
    result = n
    while True:
        result += 1 #일단 하나올려
        bin_result = bin(result)[2:] #바이너리 구해
        if bin_result.count("1") == ones:
            return result
    
    return result