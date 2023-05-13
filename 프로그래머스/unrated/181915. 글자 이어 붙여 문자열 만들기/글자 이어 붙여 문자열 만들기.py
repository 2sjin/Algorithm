def solution(my_string, index_list):    
    return "".join(my_string[i] for i in index_list)

    """
    result = ""
    for i in index_list:
        result += my_string[i]
    return result
    """