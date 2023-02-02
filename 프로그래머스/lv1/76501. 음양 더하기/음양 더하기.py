def solution(absolutes, signs):
    signs_int = [1 if t else -1 for t in signs]
    result = [absolutes[i] * signs_int[i] for i in range(len(signs))]
    return sum(result)