from itertools import product

def solution(word):
    alpha = ["A", "E", "I", "O", "U"]
    words_list = []
    
    for i in range(1, 6):
        words_list += ["".join(w) for w in product(alpha, repeat=i)]
    words_list = tuple(sorted(words_list))
    
    return words_list.index(word) + 1