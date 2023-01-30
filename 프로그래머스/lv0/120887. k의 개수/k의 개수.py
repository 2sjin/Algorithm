def solution(i, j, k):
    k_nums = [str(x) for x in range(i, j+1) if str(k) in str(x)]
    k_str = "".join(k_nums)
    answer = k_str.count(str(k))
    return answer