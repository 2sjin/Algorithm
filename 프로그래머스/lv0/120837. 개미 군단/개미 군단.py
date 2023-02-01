"""
def solution(hp):
    ants = [0 for _ in range(hp+1)]    
    
    for i in range(1, hp+1):
        if i <= 5:
            ants[i] = 1 + int(not (i%2))
        else:
            ants[i] = min(ants[i-1], ants[i-3], ants[i-5])+1
    
    return ants[-1]
"""

# 6마리의 경우, 5+1이든 3+3이든 똑같이 2마리
# 그러므로 그리디 알고리즘 적용 가능
def solution(hp):
    return (hp // 5) + ((hp % 5) // 3) + ((hp % 5) % 3)
    