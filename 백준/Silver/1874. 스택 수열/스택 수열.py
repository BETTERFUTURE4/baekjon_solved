n = int(input())
목표 = [int(input()) for _ in range(n)]
목표.reverse()
arr = [i for i in range(n,0,-1)]
stack = []
isNo = False
printResult = []

while 목표:
    if not stack or stack[-1] != 목표[-1]:
        if not arr:
            isNo = True
            break
        stack.append(arr.pop())
        printResult.append("+")
    else:
        stack.pop()
        목표.pop()
        printResult.append("-")

if isNo:
    print("NO")
else:
    for i in printResult:
        print(i)