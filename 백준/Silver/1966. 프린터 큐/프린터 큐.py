def goToEnd(dic):
    return [dic.pop()] + dic
def getMax(printer):
    return max([arr[1] for arr in printer])

t = int(input())

for _ in range(t):
    answer = 0
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    printer = []
    for i in range(n):
        printer.append([i,arr[i]])

    목표문서 = printer[m]
    printer.reverse()
    printed = []
    while printer:
        if printer[-1][1] < getMax(printer):
            printer = goToEnd(printer)
        else:
            printed.append(printer.pop())
    
    print(printed.index(목표문서)+1)