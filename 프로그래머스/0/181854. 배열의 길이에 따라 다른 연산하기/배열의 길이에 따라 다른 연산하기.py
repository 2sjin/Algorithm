def solution(arr, n):
    if len(arr) % 2 == 1:
        return [x+n if idx % 2 == 0 else x for idx, x in enumerate(arr)]                
    else:
        return [x+n if idx % 2 != 0 else x for idx, x in enumerate(arr)]