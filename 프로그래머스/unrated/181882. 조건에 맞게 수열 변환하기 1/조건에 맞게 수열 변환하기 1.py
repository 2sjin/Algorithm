def solution(arr):
    for idx, num in enumerate(arr):
        if num >= 50 and num % 2 == 0:
            arr[idx] = num // 2
        elif num < 50 and num % 2 == 1:
            arr[idx] = num * 2

    return arr