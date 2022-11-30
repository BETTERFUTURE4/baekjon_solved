X = int(input())

arr = list()
arr.append(64)

while sum(arr) > X:
    if sum(arr) == X:
        break
    cut = arr.pop() / 2

    arr.append(cut)

    if sum(arr) < X:
        arr.append(cut)

print(len(arr))