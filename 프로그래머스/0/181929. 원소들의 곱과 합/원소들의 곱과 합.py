def solution(num_list):
    hap = 0
    multi = 1

    for i in num_list:
        hap += i
        multi *= i

    return 1 if hap**2 > multi else 0