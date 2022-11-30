from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    combs =  combinations(arr[1:], 6)
    for comb in combs:
        print(*comb)
    print()