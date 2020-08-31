n = int(input())
k = int(input())
arrPhoto = list(map(int, input().split()))

dic = {}
for i in range(1, n+1):
    dic[i] = []

for i in range(k):
    x = arrPhoto[i]
    dic[x].append(i)

# 3
# 10
# 1 2 1 3 1 2 2 1 3 1
# 1---1---1-----1---1
# --2-------2-2
#       3---------3

# 3
# 3
# 1 3 3
answer = [arrPhoto[0]]
for i in range(1, n+1):
    arr1 = dic[i]
    for j in range(len(arr1)-1):
        a1 = arr1[j]
        b1 = arr1[j+1]
        canWin = True
        for k in range(1, n+1):
            if i == k:
                continue
            arr2 = dic[k]
            for m in range(len(arr2)-1):
                a2 = arr2[m]
                b2 = arr2[m+1]
                if a1 < a2 and b2 < b1:
                    canWin = False
                    break

        if canWin and i not in answer:
            answer.append(i)
            break

answer.sort()
print(len(answer))
print(' '.join(list(map(str, answer))))
