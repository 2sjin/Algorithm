def solution(s, skip, index):
    alpha = "".join(a for a in "abcdefghijklmnopqrstuvwxyz" if a not in skip)
    return "".join(alpha[(alpha.find(x)+index)%len(alpha)] for x in s)