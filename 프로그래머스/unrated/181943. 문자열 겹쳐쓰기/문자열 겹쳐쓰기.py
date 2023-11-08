def solution(my_string, overwrite_string, s):
    res = my_string[:s]
    res += overwrite_string
    res += my_string[s+len(overwrite_string):]
    return res