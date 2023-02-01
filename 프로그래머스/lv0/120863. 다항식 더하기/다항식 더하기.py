def solution(polynomial):
    cnt = [0, 0]
    
    for i in polynomial.split(" + "):
        if i == "x":
            cnt[0] += 1
        elif "x" in i:
            cnt[0] += int(i[:-1])
        else:
            cnt[1] += int(i)
    
    result = str(cnt[0]) if cnt[0] > 1 else ""
    result += "x" if cnt[0] != 0 else ""
    result += " + " if ((cnt[0] != 0) and (cnt[1] != 0)) else ""
    result += str(cnt[1]) if cnt[1] != 0 else ""
    return result.rstrip()