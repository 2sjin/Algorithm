def solution(n, s):
    if n > s:
        return [-1]
    
    result = []    
    num = s
    for i in range(n):
        result.append(num // (n-i))
        num -= num // (n-i)
    return result
