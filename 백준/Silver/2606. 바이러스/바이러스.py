def 반대노드구하기(lines, num):
    반대노드들 = list()
    for line in lines:
        if line[0] == num:
            반대노드들.append(line[1])
        elif line[1] == num:
            반대노드들.append(line[0])
    return 반대노드들

컴개수 = int(input())
연결개수 = int(input())
선배열 = list()
for _ in range(연결개수):
    선배열.append(list(map(int,input().split())))




remainNodes = set(반대노드구하기(선배열, 1))
virusCom = {1}
while len(remainNodes) > 0:
    # print("size: ",len(remainNodes), virusCom, remainNodes)
    num = remainNodes.pop()
    if num not in virusCom:
        virusCom.add(num)
        remainNodes = remainNodes.union(반대노드구하기(선배열, num))
        # print("RR")

print(len(virusCom)-1)
