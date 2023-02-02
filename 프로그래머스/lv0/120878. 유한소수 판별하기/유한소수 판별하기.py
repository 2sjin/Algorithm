from math import gcd

def prime_tuple(n):
    is_prime = [True for _ in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n+1, i):
            is_prime[j] = False
    return tuple(i for i in range(n+1) if is_prime[i] and i >= 2)

def solution(a, b):
    denom = b // gcd(a, b)
    primes = prime_tuple(denom)
    res = []
    
    while denom > 1:
        for p in primes:
            mod = denom % p
            if mod == 0:
                res.append(p)
                denom //= p
                break
    
    return 1 if sorted(list(set(res) | set([2, 5]))) == [2, 5] else 2