from math import factorial

def solution(n):
    number = 1
    cnt = 0
    
    while number <= n:
        cnt += 1        
        number *= cnt
        
    return cnt-1