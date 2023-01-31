def solution(n, k):
    total_n = 12000 * n
    total_k = 2000 * (k - n//10)
    
    answer = total_n + total_k
    return answer