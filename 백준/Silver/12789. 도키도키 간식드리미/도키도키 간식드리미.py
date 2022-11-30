N = int(input())

orders = list(reversed(list(map(int, input().split()))))

stack = []
count = 1

while orders:
    if len(stack) != 0:
        nowStack = stack.pop()
        if nowStack == count:
            count += 1
            continue
        else:
            stack.append(nowStack)
    nowOrder = orders.pop()
    if nowOrder == count:
        count += 1
        continue
    else:
        stack.append(nowOrder)

# print(orders,stack,count)

while stack:
    nowStack = stack.pop()
    if nowStack == count:
        count += 1
    else:
        break

if len(stack) == 0:
    print("Nice")
else:
    print("Sad")