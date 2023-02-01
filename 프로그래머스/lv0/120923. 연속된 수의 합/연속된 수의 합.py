def solution(num, total):
    median = total // num
    if total % num == 0:
        return tuple(range(median-(num//2), median+(num//2)+1))
    else:
        return tuple(range(median-(num//2)+1, median+(num//2)+1))