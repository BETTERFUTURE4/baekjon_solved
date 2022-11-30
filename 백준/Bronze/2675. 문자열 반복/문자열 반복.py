n = int(input())
for i in range(n):
    num, arr = input().split()
    for s in arr:
        print(s * int(num), end="")
    print()