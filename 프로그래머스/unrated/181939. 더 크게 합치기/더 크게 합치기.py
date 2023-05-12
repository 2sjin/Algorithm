def solution(a, b):
    str_a = str(a)
    str_b = str(b)
    
    return max(int(str_a+str_b), int(str_b+str_a))