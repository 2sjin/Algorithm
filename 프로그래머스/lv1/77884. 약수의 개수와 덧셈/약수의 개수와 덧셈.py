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