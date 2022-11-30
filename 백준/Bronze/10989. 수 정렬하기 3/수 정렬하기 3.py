import sys
n = int(input())

arr = [0] * 10001

for i in range(n):
    now = int(sys.stdin.readline().rstrip())
    arr[now] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)