def solution(arr):
    x = 0
    while True:
        prev_arr = arr[:] 
        
        new_arr = []
        for n in arr:
            if n >= 50 and n % 2 == 0:
                new_arr.append(n // 2)
            elif n < 50 and n % 2 == 1:
                new_arr.append(n * 2 + 1)
            else:
                new_arr.append(n)
        
        arr = new_arr
        
        if prev_arr == arr:
            return x 
        
        x += 1 