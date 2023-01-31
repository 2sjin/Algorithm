from collections import Counter

def solution(spell, dic):
    for word in dic:
        if Counter(spell) == Counter(word):
            return 1
    return 2