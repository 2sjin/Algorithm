from itertools import combinations

def solution(nums):
    comb = [sum(i) for i in combinations(nums, 3)]  # 3개 고르기(조합)
    comb_max = max(comb)    # 합계가 최대가 되는 조합

    # comb_max까지 수의 소수 여부 확인
    is_prime = [True for _ in range(comb_max+1)]
    for i in range(2, int(comb_max**0.5)+1):
        for j in range(i*2, comb_max+1, i):
            is_prime[j] = False
    
    # nums에 들어있는 숫자 중 소수 개수 리턴
    return len([i for i in comb if is_prime[i]])