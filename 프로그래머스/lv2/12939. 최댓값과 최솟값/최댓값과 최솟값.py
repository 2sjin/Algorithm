def solution(s):
    s_tuple = tuple(map(int, s.split()))

    res_min = min(s_tuple)
    res_max = max(s_tuple)
    answer = str(res_min) + " " + str(res_max)
    
    return answer