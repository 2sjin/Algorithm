from collections import Counter

def solution(clothes):
    cnts = Counter([x[1] for x in clothes])
    
    answer = 1
    for i in [x+1 for x in cnts.values()]:
        answer *= i
    
    return answer-1