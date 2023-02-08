def solution(skill, skill_trees):
    answer = len(skill_trees)

    for s_tree in skill_trees:
        for idx, ch in enumerate([x for x in s_tree if x in skill]):
            if ch != skill[idx]:
                answer -= 1
                break

    return answer