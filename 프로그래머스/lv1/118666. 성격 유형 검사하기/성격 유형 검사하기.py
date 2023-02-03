def solution(survey, choices):
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
    
    result = ""
    for x in ("RT", "CF", "JM", "AN"):
        result += x[0] if dic[x[0]] >= dic[x[1]] else x[1]
    return result