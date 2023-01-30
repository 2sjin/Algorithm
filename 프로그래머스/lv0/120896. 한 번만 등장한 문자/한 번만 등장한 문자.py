from collections import Counter

def solution(s):
    answer = ''
    
    cnts = Counter(s)
    for k, v in cnts.items():
        if v == 1:
            answer += k
            
    answer = "".join(sorted(answer))
    
    return answer