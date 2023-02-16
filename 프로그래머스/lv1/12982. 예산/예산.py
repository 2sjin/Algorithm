def solution(d, budget):
    result = 0
    for i in sorted(d):
        if budget >= i:
            budget -= i
            result += 1
    return result