n = int(input())
k = int(input())
arrPhoto = input().split()

s = '.'.join(arrPhoto)
s += '.'

arr = []

for i in range(1, n+1):
    sub = s.split(str(i)+'.')
    last = -1
    for j in range(len(arrPhoto)):
        if arrPhoto[j] == i:
            if last+1 == j:
                arr.append(i)
                break
            last = j


arr.sort()
print(len(arr))
print(' '.join(list(map(str, arr))))
