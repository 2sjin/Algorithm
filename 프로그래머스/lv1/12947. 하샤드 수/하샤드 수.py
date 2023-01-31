def solution(x):
    return x % sum(map(int, tuple(str(x)))) == 0