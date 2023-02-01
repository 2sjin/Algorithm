from collections import Counter

def solution(lines):
    dic = {}
    res = []
    
    for i in lines:
        res += range(i[0], i[1])
        
    dic = Counter(res)
    return len([i[0] for i in dic.items() if i[1] >= 2])