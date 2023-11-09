def solution(ineq, eq, n, m):
    comp = (ineq + eq).replace("!", "")
    return int(eval(str(n) + comp + str(m)))