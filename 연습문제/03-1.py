import sys

for i in range(1, 1001):
    print(i)
    sys.stdout.flush()
    reply = input()
    if reply == 'CORRECT':
        break
    elif reply == 'UP':
        continue
    elif reply == 'DOWN':
        continue
