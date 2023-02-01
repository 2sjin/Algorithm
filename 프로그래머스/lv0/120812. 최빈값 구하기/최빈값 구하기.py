def solution(array):
    dic = {}

    for key in set(array):
        dic[key] = array.count(key)
    
    items = sorted(dic.items(), key=lambda x: x[1])
    
    return -1 if len(items) >= 2 and (items[-1][1] == items[-2][1]) else items[-1][0]