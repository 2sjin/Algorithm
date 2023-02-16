from collections import Counter

def solution(X, Y):
    result = ""
    cnt_X = dict(Counter(X))
    cnt_Y = dict(Counter(Y))
    
    for i in "9876543210":
        try:
            result += i * min(cnt_X[i], cnt_Y[i])
        except:
            continue

    if result == "":
        return "-1"
    elif result[0] + result[-1] == "00":
        return "0"
    return result