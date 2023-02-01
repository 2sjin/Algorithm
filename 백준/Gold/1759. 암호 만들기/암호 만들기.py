from itertools import *

L, C = map(int, input().split())

char_list = list(input().split())
pwd_list = set()

for pw in tuple(combinations(char_list, L)):
    cnt_a, cnt_b = 0, 0
    for a in "aeiou":
        if a in pw:
            cnt_a += 1
    for b in "bcdfghjklmnpqrstvwxyz":
        if b in pw:
            cnt_b += 1
    if cnt_a >= 1 and cnt_b >= 2:
        pwd_list.add(''.join(sorted(pw)))

pwd_list = sorted(list(pwd_list))

print('\n'.join(pwd_list))