num = int(input())
arr = list()
for i in range(num):
    arr.append(input())
arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)
