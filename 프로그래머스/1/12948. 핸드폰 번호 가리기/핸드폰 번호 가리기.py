def solution(phone_number):
    last = phone_number[-4:]
    fir = "".join(["*" for i in range(len(phone_number)-4)])

    return fir + last