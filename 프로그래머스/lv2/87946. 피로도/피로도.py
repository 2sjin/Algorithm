from itertools import permutations

def solution(k, dungeons):
    perm = [x for x in permutations(dungeons)]
    max_cnt = 0
    
    for p in perm:
        stress = k
        cnt = 0

        for require, consume in p:
            if stress >= require:
                stress -= consume
                cnt += 1
            else:
                break
                
        if cnt > max_cnt:
            max_cnt = cnt
            
    return max_cnt