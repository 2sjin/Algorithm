def solution(k, m, score):
    score_sorted = sorted(score, reverse=True)
    
    result = 0
    for i in range(0, len(score), m):
        box = score_sorted[i:i+m]
        if len(box) == m:
            result += min(box) * m
    
    return result