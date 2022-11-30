def getAllRoute(arr, x,y):
    stackArr = [[[x,y], str(arr[y][x])]]
    # print("stackArr", stackArr)
    result = []
    while stackArr:
        node = stackArr.pop()
        # print("node[1]", node[1])
        if len(node[1]) == 6:
            result.append(node[1])
        else:
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]
            x = node[0][0]
            y = node[0][1]
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < 5 and 0 <= yy < 5:
                    stackArr.append([[xx,yy], node[1] + str(arr[yy][xx])])
    return result

arr = [list(map(int, input().split()))for _ in range(5)]
# print(arr)

routes = set()
for x in range(5):
    for y in range(5):
        routes = routes.union(getAllRoute(arr, x,y))

print(len(routes))