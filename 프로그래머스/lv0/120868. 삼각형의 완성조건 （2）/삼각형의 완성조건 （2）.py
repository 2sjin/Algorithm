def solution(sides):
    longs = max(sides)
    shorts = min(sides)
    return len(range(longs-shorts+1, longs+shorts))

# 가장 긴 변이 6인 경우  : 4(=6-3+1) ~ 6
# 나머지 한 변이 가장 긴 경우 : 7(6+1) ~ 8(3+6-1)

# 가장 긴 변이 11인 경우 : 5(=11-7+1) ~ 11
# 나머지 한 변이 가장 긴 경우 : 12(11+1) ~ 17(11+7-1)