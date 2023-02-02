def prime_tuple(n):
    is_prime = [True for _ in range(n+1)]
    
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    
    return tuple(i for i in range(n+1) if is_prime[i] and i >= 2)

def solution(n):
    primes = prime_tuple(n)     # n 이하의 소수 튜플

    answer = []
    
    number = n
    while number > 1:
        for p in primes:
            mod = number % p
            if mod == 0:
                answer.append(p)
                number //= p
                break
                
    return sorted(list(set(answer)))