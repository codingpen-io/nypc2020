def solve(arr, x, y, n):
    print('solve', 'x', x, 'y', y)
    chair = []
    if arr[y][x] == '0':
        arr[y][x] = 'c'  # chair, 의자
        chair.append([x, y])
        # 의자가 놓아지면 주변에 거리 두기
        around = [
            [-1, -1], [0, -1], [1, -1],
            [-1, 0],           [1, 0],
            [1, 1], [0, 1], [1, 1],
        ]
        for a in around:
            ax = x + a[0]
            ay = y + a[1]
            if ax >= 0 and ax <= n - 1 and ay >= 0 and ay <= n-1:
                if arr[ay][ax] == '0':
                    arr[ay][ax] = '-'  # space 거리

    if x == 4 and y == 4:
        print('bingo')
    x += 1
    if x > n-1:
        x = 0
        y += 1
        if y > n-1:
            print('exit end')
            return chair

    s = solve(arr, x, y, n)
    print('chair', type(chair), 'type', type(s))
    if len(s) > 0:
        print('extend')
        t = chair.extend(s)
        if t == None:
            print('bingo')
        return t
    print('return chair')
    return chair


files = ['./예선1일차/input_15_1.txt']
# files = ['./input_15_1.txt']
for file in files:
    f = open(file)
    s = f.readline()
    n, k = map(int, s.split())
    arr = []
    for i in range(n):
        arr.append(['0']*n)
    for i in range(k):
        s = f.readline()
        x, y = map(int, s.split())
        print(x, y)
        arr[y-1][x-1] = 'x'  # 장애물

    max = []
    for i in range(n):
        for j in range(n):
            r = solve(arr[:], 0, 0, n)
            if len(r) > len(max):
                max = r

    # print('dotori', dotori)
    print(len(max))
    for x in max:
        print(x[0], x[1])
    f.close()
