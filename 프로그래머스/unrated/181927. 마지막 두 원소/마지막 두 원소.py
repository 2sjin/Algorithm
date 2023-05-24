def solution(num_list):
    last_e = num_list[-1]
    prev_e = num_list[-2]
    return num_list + [last_e-prev_e if last_e>prev_e else last_e*2]