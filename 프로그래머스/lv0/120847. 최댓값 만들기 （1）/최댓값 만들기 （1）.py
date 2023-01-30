def solution(numbers):
    nlist = sorted(numbers, reverse=True)
    answer = nlist[0] * nlist[1]
    return answer