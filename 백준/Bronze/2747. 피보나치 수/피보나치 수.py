N = int(input())

nlist = [0, 1]

for i in range(2, N+1):
    nlist.append(nlist[i-2] + nlist[i-1])

print(nlist[N])