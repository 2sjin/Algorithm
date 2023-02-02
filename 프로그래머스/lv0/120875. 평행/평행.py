from collections import Counter

def solution(dots):
    # 기울기: y증가량 / x증가량
    slopes = []
    for d1, d2 in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)):
        x_inc = abs(dots[d1][0] - dots[d2][0])
        y_inc = abs(dots[d1][1] - dots[d2][1])
        slopes.append(y_inc / x_inc)
    
    return 1 if max(Counter(slopes).values()) >= 2 else 0