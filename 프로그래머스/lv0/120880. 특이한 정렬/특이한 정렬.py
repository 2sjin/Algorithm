"""
def solution(numlist, n):
    dic = {}
    order = [abs(n-i) for i in numlist]
    for i in range(len(numlist)):
        dic[numlist[i]] = order[i] 
    res = sorted(dic.items(), key=lambda x: (x[1], x[0] * -1))
    return [i[0] for i in res]
"""

# 숏코딩
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(n-x), -x))