a = input().split()

print((int(a[0]) + int(a[1])) % int(a[2]))
print(((int(a[0]) % int(a[2])) + (int(a[1]) % int(a[2]))) % int(a[2]))
print((int(a[0]) * int(a[1])) % int(a[2]))
print(((int(a[0]) % int(a[2])) * (int(a[1]) % int(a[2]))) % int(a[2]))