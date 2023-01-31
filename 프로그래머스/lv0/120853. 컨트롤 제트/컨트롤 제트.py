def solution(s):
    s_split = s.split()
    answer = 0
    for i in enumerate(s_split):
        if i[1] == "Z":
            answer -= int(s_split[i[0]-1])
        else:
            answer += int(i[1])
    
    return answer