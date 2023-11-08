def solution(todo_list, finished):
    res = []
    for i in range(len(todo_list)):
        if not finished[i]:
            res.append(todo_list[i])
    return res