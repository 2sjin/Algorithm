def solution(s):
    result = [-1 for i in range(len(s))]
    dic = {}
    for i, ch in enumerate(s):
        if ch in dic.keys():
            result[i] = i - dic[ch]
        dic[ch] = i
            
    return(result)