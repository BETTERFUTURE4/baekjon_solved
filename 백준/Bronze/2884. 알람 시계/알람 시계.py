hour, minite = map(int, input().split())

if minite < 45:
    if hour == 0:
        print(23 , minite+15)
    else:
        print(hour-1 , minite+15)

else:
    print(hour, minite - 45)