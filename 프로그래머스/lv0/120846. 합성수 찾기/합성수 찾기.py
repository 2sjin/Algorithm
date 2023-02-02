def solution(n):
    prime = [True for _ in range(n+1)]
    
    for i in range(2, int(n**0.5)+1):
        for mul in range(i*2, n+1, i):
            prime[mul] = False
    
    return len([tf for tf in prime[2:] if not tf])