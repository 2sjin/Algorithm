"""
def solution(s1, s2):
    answer = 0
    for s in s1:
        if s in s2:
            answer += 1 if s in s2
    return answer
"""

# 집합(set) 사용
def solution(s1, s2):
    answer = len(set(s1) & set(s2)) # 교집합
    return answer