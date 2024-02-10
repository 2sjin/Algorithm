n = int(input())

for i in range(1, n+1):
    num = str(i)
    for j in ("3", "6", "9"):
        num = num.replace(j, "-")

    if "-" in num:
        for _ in range(num.count("-")):                   
            print("-", end="")
        print("", end=" ")
    else:
        print(i, end=" ")