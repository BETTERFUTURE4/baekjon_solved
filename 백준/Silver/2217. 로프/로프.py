N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort(reverse=True)
result = list()
for i in range(1, N+1):
    result.append(arr[i-1] * i)

print(max(result))
