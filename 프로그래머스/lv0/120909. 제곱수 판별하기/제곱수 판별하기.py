from math import sqrt

def solution(n):
    answer = 1 if sqrt(n) == int(sqrt(n)) else 2
    return answer