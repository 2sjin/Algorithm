import sys

dic = {1:1, 2:1}

def fibo(x):
    if x in (1, 2):
        return 1

    if x in dic.keys():
        return dic[x]
    
    dic[x] = fibo(x-1) + fibo(x-2)
    return dic[x]
    
n = int(sys.stdin.readline().rstrip())
print(fibo(n))
