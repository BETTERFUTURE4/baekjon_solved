N = int(input())
arr = sorted(list(map(int, input().split())))

sumArr = [sum(arr[:i+1]) for i in range(len(arr))]
print(sum(sumArr))