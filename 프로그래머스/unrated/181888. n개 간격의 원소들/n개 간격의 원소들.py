def solution(num_list, n):
    res = []
    for i in range(0, len(num_list), n):
        res.append(num_list[i])
    return res