from math import gcd

def solution(n, m):
    return (lambda x: [x, n*m//x])(gcd(n, m))