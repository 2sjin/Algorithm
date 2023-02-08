def solution(n, arr1, arr2):
    answer = [bin(arr1[i]|arr2[i]) for i in range(n)]
    return [x[2:].zfill(n).replace("0", " ").replace("1", "#") for x in answer]