N = int(input())
cardArr = list(map(int, input().split()))
M = int(input())
needCardArr = list(map(int, input().split()))
result = ""

dictArr = dict()
for c in cardArr:
    dictArr[c] = 0

for c in cardArr:
    dictArr[c] += 1

for need in needCardArr:
    if need not in dictArr.keys():
        result += " 0"
    else:
        result += " " + str(dictArr[need])

print(result[1:])