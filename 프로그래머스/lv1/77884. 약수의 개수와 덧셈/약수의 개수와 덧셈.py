"""
def divisor_count(n):    
    cnt = 2 if n != 1 else 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            cnt += 2 if n != i**2 else 1
    return cnt

def solution(left, right):
    nums = [i for i in range (left, right+1)]
    signs = []
    for i in range(left, right+1):
        signs.append(1 if divisor_count(i)%2 == 0 else -1)
        
    return sum(z[0]*z[1] for z in (zip(nums, signs)))
"""

# 아래 성질을 안다고 가정한 풀이
# '완전제곱수는 약수가 홀수 개, 이외의 수는 약수가 짝수 개'
def solution(left, right):
    nums = [i for i in range(left, right+1)]
    signs = [-1 if n**0.5 == int(n**0.5) else 1 for n in nums]
    return sum(z[0]*z[1] for z in zip(nums, signs))