def solution(answers):    
    sol = ((1, 2, 3, 4, 5),
           (2, 1, 2, 3, 2, 4, 2, 5),
           (3, 3, 1, 1, 2, 2, 4, 4, 5, 5))
    sol_length = (5, 8, 10) 
    result = {1:0, 2:0, 3:0}
    
    for ans in range(len(answers)):
        for std in range(3):        
            result[std+1] += 1 if answers[ans] == sol[std][ans%sol_length[std]] else 0
                
    max_score = max(result.values())
    return [i[0] for i in result.items() if i[1] == max_score]