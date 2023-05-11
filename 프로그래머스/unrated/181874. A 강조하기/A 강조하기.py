def solution(myString):
    answer = ''
    
    for s in myString:
        answer += s.upper() if s in "Aa" else s.lower()
    
    return answer