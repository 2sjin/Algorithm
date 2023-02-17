def solution(n, lost, reserve):
    intersection = set(lost) & set(reserve)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)
    
    answer = n - len(lost)
    
    for x in lost:
        if x-1 in reserve:
            reserve.remove(x-1)
            answer += 1
        elif x+1 in reserve:
            reserve.remove(x+1)
            answer += 1
            
    return answer