def solution(score):
    rank_dic = {}
    score_avg = [sum(i)/2 for i in score]
    for rank, avg in enumerate(sorted(score_avg, reverse=True), start=1):
        if avg not in rank_dic.keys():
            rank_dic[avg] = rank
    return [rank_dic[i] for i in score_avg]