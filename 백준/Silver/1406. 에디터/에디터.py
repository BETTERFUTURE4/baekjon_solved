import sys

strs = list(sys.stdin.readline().rstrip())
cusorNext = []
M = int(input())
commands = [sys.stdin.readline().split() for _ in range(M)]

for command in commands:
    if command[0] == 'L' and len(strs) > 0:
        cusorNext.append(strs.pop())
    elif command[0] == 'D' and len(cusorNext) > 0:
        strs.append(cusorNext.pop())
    elif command[0] == 'B' and len(strs) > 0:
        strs.pop()
    elif command[0] == 'P':
        strs.append(command[1])

print(''.join(strs + list(reversed(cusorNext))))