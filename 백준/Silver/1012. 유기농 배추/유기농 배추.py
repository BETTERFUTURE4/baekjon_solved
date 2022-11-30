def 인근배추삭제(inb, bat):
    arr = [inb]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while arr:
        배추위치 = arr.pop(0)
        for i in range(4):
            ix = 배추위치[0] + dx[i]
            iy = 배추위치[1] + dy[i]
            if 0 <= ix < M and 0 <= iy < N and bat[iy][ix] == 1:
                bat[iy][ix] = 0
                arr.append([ix,iy])

T = int(input())
countArr = list()

for _ in range(T):
    M,N,K = map(int, input().split())

    배추위치s = [list(map(int,input().split())) for _ in range(K)]

    bat = [[0 for _ in range(M)] for _ in range(N)]
    for 위치 in 배추위치s:
        bat[위치[1]][위치[0]] = 1

    count = 0
    for x_ in range(M):
        for y_ in range(N):
            if bat[y_][x_] == 1:
                인근배추삭제([x_,y_], bat)
                count += 1

    countArr.append(count)

for i in countArr:
    print(i)
