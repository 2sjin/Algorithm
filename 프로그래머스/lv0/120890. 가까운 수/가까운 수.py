def solution(array, n):
    dic = {}
    for i in array:
        dic[i] = abs(n-i)
    min_d = min(dic.values())
    result = [i for i in dic.keys() if dic[i] == min_d]
    return min(result)