"""
from math import factorial

def solution(balls, share):
    answer = factorial(balls) // (factorial(balls-share) * factorial(share))
    return answer
"""

from math import comb

def solution(balls, share):
    return comb(balls, share)