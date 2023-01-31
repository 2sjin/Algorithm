def solution(s):
    for ch in s:
        if ch.isalpha():
            return False
    
    return True if len(s) in (4, 6) else False