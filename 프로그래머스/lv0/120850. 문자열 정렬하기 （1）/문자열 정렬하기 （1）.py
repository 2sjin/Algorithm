def solution(my_string):
    digit_list = [int(i) for i in my_string if i.isdigit()]
    digit_list.sort()
    answer = digit_list
    return answer