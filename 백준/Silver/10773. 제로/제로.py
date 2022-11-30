num = int(input())
arr = list()
for i in range(num):
    temp = int(input())
    if temp == 0 and len(arr) != 0:
        arr.pop()
    else:
        arr.append(temp)   

print(sum(arr))