from itertools import combinations

def solution(numbers):
    answer = tuple(i[0]*i[1] for i in combinations(numbers, 2))
    return max(answer)