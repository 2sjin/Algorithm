T = int(input())

for test_case in range(1, T+1):
    score_G = [1, 2, 3, 3, 4, 10]
    score_E = [1, 2, 2, 2, 3, 5, 10]

    team_G = list(map(int, input().split()))
    team_E = list(map(int, input().split()))

    res_G = sum([score_G[i] * team_G[i] for i in range(6)])
    res_E = sum([score_E[i] * team_E[i] for i in range(7)])

    print(f"Battle {test_case}: ", end="")
    if res_G > res_E:
        print("Good triumphs over Evil")
    elif res_G < res_E:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")