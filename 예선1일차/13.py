import sys
sys.setrecursionlimit(100000)

R, C = map(int, input().split())
S = input()

arr = []
visit = []

count = 0
for i in range(R):
    s = list(input())
    arr.append(s)
    visit.append([0] * len(s))


def fill(x, y, prevValue):
    if x < 0 or x > C - 1 or y < 0 or y > R - 1:
        return
    if visit[y][x] == 1:
        return
    # print('fill', x, y)
    v = arr[y][x]
    if v == '?':
        if S == 'min':
            arr[y][x] = prevValue
        else:
            if prevValue == 'L':
                arr[y][x] = 'S'
            else:
                arr[y][x] = 'L'
        v = arr[y][x]
        visit[y][x] = 1
    else:
        visit[y][x] = 1

    fill(x-1, y, v)
    fill(x+1, y, v)
    fill(x, y-1, v)
    fill(x, y+1, v)


fill(0, 0, 'S')


def count_robot(x, y, preValue):
    if x < 0 or x > C - 1 or y < 0 or y > R - 1:
        return 0
    if arr[y][x] == -1:
        return 0
    v = arr[y][x]
    myCount = 0
    if preValue == 'S' and v == 'L':
        myCount += 1

    arr[y][x] = -1
    myCount += count_robot(x-1, y, v)
    myCount += count_robot(x+1, y, v)
    myCount += count_robot(x, y-1, v)
    myCount += count_robot(x, y+1, v)
    return myCount


count = count_robot(0, 0, 'S')
print(count)
