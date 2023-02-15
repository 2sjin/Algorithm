def divisor(num):
    cnt = 2
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            cnt += 2
    return cnt if (num**0.5) != int(num**0.5) else cnt-1

def solution(number, limit, power):
    result = 0
    for i in range(number):
        div = divisor(i+1)
        result += div if div <= limit else power
    return result
        