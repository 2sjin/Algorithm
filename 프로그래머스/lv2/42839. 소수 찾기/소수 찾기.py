from itertools import permutations

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True        

def solution(numbers):
    perms = []
    for i in range(1, len(numbers)+1):
        perms += permutations(numbers, i)
    perms = set(map(int, ["".join(x) for x in perms]))
    return len([x for x in perms if isprime(x)])