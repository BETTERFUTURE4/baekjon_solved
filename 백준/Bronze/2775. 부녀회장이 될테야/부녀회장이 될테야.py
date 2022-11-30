t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    
    arr = [i+1 for i in range(n)]
    for kn in range(k):
        for nn in range(n):
            arr.append(sum(arr[kn*n : kn*n + nn+1]))
    print(arr[len(arr)-1])