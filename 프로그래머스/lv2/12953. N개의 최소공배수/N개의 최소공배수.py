from math import gcd

def solution(arr):
    lcm = 1
    for i in arr:
        lcm = lcm * i // gcd(lcm, i)
    return lcm