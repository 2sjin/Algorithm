def solution(a, b):
    step = 1 if a < b else -1
    return sum(range(a, b+step, step))