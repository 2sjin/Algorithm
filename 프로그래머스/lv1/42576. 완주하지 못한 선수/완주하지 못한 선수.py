def solution(participant, completion):
    dic = {}
    sum_hash = 0
    
    for x in participant:
        dic[hash(x)] = x
        sum_hash += hash(x)
        
    for x in completion:
        sum_hash -= hash(x)
        
    return dic[sum_hash]