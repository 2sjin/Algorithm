def solution(arr, delete_list):
    for x in delete_list:
        try:
            arr.remove(x)
        except:
            continue
    return arr