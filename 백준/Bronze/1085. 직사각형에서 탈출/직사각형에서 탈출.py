x,y,w,h = map(int, input().split())

arr = [h-y,y,w-x,x]
print(min(arr))