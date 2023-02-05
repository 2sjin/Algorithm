def solution(a, b):
    day_of_the_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month_to_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    
    result = sum(month_to_day[:a]) + b - 1
    return day_of_the_week[result % 7]