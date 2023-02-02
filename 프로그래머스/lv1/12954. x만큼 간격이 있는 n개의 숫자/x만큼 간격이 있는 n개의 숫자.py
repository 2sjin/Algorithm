"""
def solution(x, n):
    return [i for i in range(x, x*n+(x//abs(x)), x)] if x != 0 else [0 for i in range(n)]
"""

def solution(x, n):
    return [x + (x*i) for i in range(n)]