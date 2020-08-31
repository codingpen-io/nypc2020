R, C = map(int, input().split())
S = input()

arr = []

count = 0
for i in range(R):
    s = input()
    if S == 'min':
        s = s.replace('?', 'S')
    else:
        for j in range(len(s)):
            if s[j] == '?':

    arr.append(s)

for i in range(len(arr)):
    s = arr[i]
    canCount = True
    for c in s:
        if c == 'L' and canCount == True:
            canCount = False
            count += 1
        else:
            canCount = True


print(count)
