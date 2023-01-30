from itertools import permutations

def solution(numbers):
    answer = tuple(permutations(numbers, 2))
    answer = tuple(set(map(sum, answer)))
    answer = sorted(answer)
    return answer