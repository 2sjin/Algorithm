"""
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
"""

# 소인수가 2와 5만 존재 -> 나머지가 없도록 2와 5로 계속 나누다보면, 1이 되어야 함
from math import gcd
def solution(a, b):
    denom = b // gcd(a, b)
    while denom % 2 == 0:
        denom //= 2
    while denom % 5 == 0:
        denom //= 5
    
    return 1 if denom == 1 else 2