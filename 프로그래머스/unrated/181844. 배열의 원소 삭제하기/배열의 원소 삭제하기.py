def solution(arr, delete_list):
    return [x for x in arr if x not in delete_list]
    
    """
    for x in delete_list:
        try:
            arr.remove(x)
        except:
            continue
    return arr
    """