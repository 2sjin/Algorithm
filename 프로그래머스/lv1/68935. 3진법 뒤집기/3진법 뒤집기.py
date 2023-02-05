def solution(n):
    trit = ""
    while n >= 1:
        trit += str(n%3)
        n //= 3
    
    return int(trit, 3)