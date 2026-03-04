def solution(myString, pat):
    answer = ''
    lengh = len(pat)
    idx = myString.rfind(pat)
    return myString[:idx+lengh]