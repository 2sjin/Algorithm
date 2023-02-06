def solution(t, p):
    len_t, len_p = len(t), len(p)
    num_list = list(map(int, [t[i:i+len_p] for i in range(len_t-len_p+1)]))
    return len([i for i in num_list if i <= int(p)])