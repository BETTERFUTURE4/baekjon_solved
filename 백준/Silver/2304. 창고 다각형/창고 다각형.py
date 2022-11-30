def getSize2(arr):
    maxIdx = sorted(arr, key=lambda arr: arr[0]).pop()[0]
    matrix = [[0,0] for _ in range(1001)]
    for a in arr:
        matrix[a[0]] = a
    # print(matrix)
    result = 0
    maxCheck = 0
    # print("maxIdx", maxIdx)

    highstIdx = sorted(arr, key=lambda arr: arr[1]).pop()[0]
    # print("highstIdx", highstIdx)

    for i in range(0, highstIdx):
        # print("maxCheck",i, maxCheck)
        maxCheck = max(maxCheck, matrix[i][1])
        result += maxCheck

    # print()
    maxCheck = 0
    for i in range(maxIdx, highstIdx, -1):
        # print("maxCheck",i, maxCheck, matrix[i][1])
        maxCheck = max(maxCheck, matrix[i][1])
        result += maxCheck

    result += matrix[highstIdx][1]
    return result

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda arr: arr[0])

result = getSize2(arr)

print(result)