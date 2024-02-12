def grade_to_score(grade):
    if grade == "A+":
        return 4.5
    if grade == "A0":
        return 4.0
    if grade == "B+":
        return 3.5
    if grade == "B0":
        return 3.0
    if grade == "C+":
        return 2.5
    if grade == "C0":
        return 2.0
    if grade == "D+":
        return 1.5
    if grade == "D0":
        return 1.0
    else:
        return 0.0

total_score = 0
total_credit = 0
for _ in range(20):
    name, credit, grade = input().split()
    credit = float(credit)

    if grade != "P":    
        total_score += (credit * grade_to_score(grade))
        total_credit += credit

print(total_score / total_credit)