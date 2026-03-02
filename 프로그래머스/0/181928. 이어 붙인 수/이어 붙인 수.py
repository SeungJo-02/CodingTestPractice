def solution(num_list):
    addOdd = ""
    addEven = ""

    for i in num_list:
        if i % 2 == 1:
            addOdd += str(i)
        else:
            addEven += str(i)
    return int(addOdd) + int(addEven)