def solution(s):
    result = 0
    flag = 0    
    first_char = s[0]
    
    for i, ch in enumerate(s):
        flag += 1 if ch == first_char else -1
        if flag == 0:
            result += 1
            first_char = s[i+1] if i+1 < len(s) else s[-1]
        
    if flag != 0:
        result += 1
    
    return result