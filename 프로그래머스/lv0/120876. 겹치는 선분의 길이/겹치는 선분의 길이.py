"""
from collections import Counter

def solution(lines):
    dic = {}
    res = []
    
    for i in lines:
        res += range(i[0], i[1])
        
    dic = Counter(res)
    return len([i[0] for i in dic.items() if i[1] >= 2])
"""

# 집합 사용해서 풀기
def solution(lines):
    sets = [set(range(lines[i][0], lines[i][1])) for i in range(3)]
    return len(sets[0] & sets[1] | sets[1] & sets[2] | sets[2] & sets[0])