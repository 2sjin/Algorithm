def solution(hp):
    ants = [0 for _ in range(hp+1)]    
    
    for i in range(1, hp+1):
        if i <= 5:
            ants[i] = 1 + int(not (i%2))
        else:
            ants[i] = min(ants[i-1], ants[i-3], ants[i-5])+1
    
    return ants[-1]