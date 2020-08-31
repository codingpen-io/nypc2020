n = int(input())
k = int(input())
arrPhoto = list(map(int, input().split()))

answer = set()
# answer.add(arrPhoto[0])

begin = 0
end = 1

# 1 2 3 1


def find_dup(arr, skip):
    r = []
    for n in arr:
        if skip == n:
            continue
        if arr.count(n) > 1:
            r.append(n)
    return r


while end <= k-1 and begin < k-1:
    # print(arrPhoto[begin], arrPhoto[end])
    b = arrPhoto[begin]
    e = arrPhoto[end]
    if arrPhoto[begin] == arrPhoto[end]:
        dup = find_dup(arrPhoto[begin:end+1], arrPhoto[begin])
        #print(begin, end, dup)
        for n in dup:
            answer.add(n)

        begin = end + 1
        end = begin + 1
    else:
        end += 1


answer = list(answer)
answer.sort()

print(len(answer))
print(' '.join(list(map(str, answer))))
