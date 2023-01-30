from math import gcd

def solution(numer1, denom1, numer2, denom2):
    res_numer = (numer1 * denom2) + (numer2 * denom1)
    res_denom = denom1 * denom2
    
    res_gcd = gcd(res_numer, res_denom)
    res_numer //= res_gcd
    res_denom //= res_gcd
    
    answer = [res_numer, res_denom]
    return answer