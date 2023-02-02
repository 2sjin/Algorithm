def solution(n):
    is_prime = [True for _ in range(n+1)]
    
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            is_prime[j] = False
            
    return is_prime[2:].count(True)