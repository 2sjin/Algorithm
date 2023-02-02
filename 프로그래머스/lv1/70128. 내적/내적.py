"""
def solution(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))
"""

# zip 함수 활용
def solution(a, b):
    return sum(i*j for i, j in tuple(zip(a, b)))