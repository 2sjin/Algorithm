def blank_list(s):
    blist = [] if s[0] == " " else [0]
    cnt = 0
    for ch in s:
        if ch == " ":
            cnt += 1
        elif cnt >= 1:
            blist.append(cnt)
            cnt = 0
    if cnt >= 1:
        blist.append(cnt)
    return blist

def solution(s):
    blanks = blank_list(s)
    answer = " " * blanks.pop(0)
    s_list = s.split()
    for ch in s_list:
        for i in range(len(ch)):
            answer += ch[i].upper() if i%2==0 else ch[i].lower()
        answer += " " * blanks.pop(0) if blanks else ""
    return answer