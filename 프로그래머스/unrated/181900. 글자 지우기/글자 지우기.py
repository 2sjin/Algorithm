def solution(my_string, indices):
    res = list(my_string)
    for i in indices:
        res[i] = ''
    return ''.join(res)