def solution(myString):
    for i,v in enumerate(myString):
        if v < "l":
            myString = myString.replace(v,"l")
            
    return myString