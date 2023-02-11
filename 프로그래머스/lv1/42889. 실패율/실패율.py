def solution(N, stages):
    clear_rates = {}
    arrive = [0 for _ in range(N+1)]
    
    for i in stages:
        for j in range(i):
            arrive[j] += 1
            
    for i in range(N):
        clear_rates[i+1] = (arrive[i]-arrive[i+1]) / arrive[i] if arrive[i] != 0 else 0
    
    clear_rates_sorted = sorted(clear_rates.items(), key=lambda x: (-x[1], x[0]))
    
    return [x[0] for x in clear_rates_sorted]