def solution(sizes):    
    size_max = []
    size_min = []
    for s in sizes:
        size_max.append(max(s))
        size_min.append(min(s))
    return max(size_max) * max(size_min)