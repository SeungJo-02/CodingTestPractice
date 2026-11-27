import datetime
def solution(a, b):
    t = datetime.date(2016,a,b)#날짜 객체 생성
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return days[t.weekday()]#요일의 번호를 알려줌(월:0,일:6)