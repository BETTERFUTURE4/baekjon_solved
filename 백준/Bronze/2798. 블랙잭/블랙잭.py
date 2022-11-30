import itertools

n, m = map(int, input().split())

cards = list(map(int, input().split()))

combs = itertools.combinations(cards, 3)
max = 0;
for comb in combs:
    sumcb = sum(comb)
    if sumcb > max and sumcb <= m:
        max = sumcb
print(max)