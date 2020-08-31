import sys
n = int(input())
arr = []

if n < 2:
    print('0')
    sys.exit()

for i in range(n):
    t = list(map(int, input().split(":")))
    arr.append(t[0]*6000 + t[1]*100 + t[2])

arr.sort()
c = 0
if n % 2 == 0:
    best = arr[n//2-1] + arr[n//2]
    del arr[n//2-1]
    del arr[n//2-1]
else:
    best = arr[n//2 - 1] + arr[n//2 + 1]
    del arr[n//2 - 1]
    del arr[n//2]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] - best < 1000:
            c += 1
            arr[i] += 10000
            arr[j] += 10000

print(c+1)
