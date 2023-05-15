def solution(a, b):
    # a, b 모두 홀수 -> a*b가 홀수
    if (a*b) % 2 == 1:
        return (a**2) + (b**2)
    
    # a, b 중 하나만 홀수 -> a+b가 홀수
    elif (a+b) % 2 == 1:
        return 2 * (a+b)
    
    # a, b 모두 짝수
    else:
        return abs(a-b)