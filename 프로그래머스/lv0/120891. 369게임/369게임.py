def solution(order):
    answer = 0
    
    for ch in str(order):
        if ch in "369":
            answer += 1

    return answer