def check_cell(arr, x, y, n, depth):
    # print(' ' * depth * 3, '   check_cell', x, y, end=' : ')
    stop = False
    down = False
    if x < 0 or x > n-1:
        dotori = 0
        stop = True
    else:
        line = arr[y]
        dotori = 0
        if line[x] == 'U':
            stop = True
        else:
            if line[x] == 'D':
                dotori = 1
            if y < n-1:
                lineBelow = arr[y+1]
                if lineBelow[x] != 'U':
                    down = True
    # print('dotori:', dotori, ', stop:', stop, ', down:', down)
    return dotori, stop, down


def solve(arr, x, y, n, depth):
    print(' ' * depth * 3, '-----------------------')
    print(' ' * depth * 3, depth, ': solve', x, y)
    path = []
    arrDown = set()
    dotori, stop, down = check_cell(arr, x, y, n, depth)
    canAppendDown = True
    if down:
        arrDown.add(x)
        canAppendDown = False

    direction = -1
    if x == 2 and y == 3:
        print('bingo')

    visit = []
    while True:
        d, stop, down = check_cell(arr, x+direction, y, n, depth)
        if stop:
            if direction == -1:
                direction = 1
                continue
            else:
                break

        x += direction
        if direction == -1:
            path.append('L')
        else:
            path.append('R')

        if x not in visit:
            dotori += d
            visit.append(x)

        if down:
            if canAppendDown:
                arrDown.add(x)
                canAppendDown = False
        else:
            canAppendDown = True

    subMaxDotori = 0
    subMaxPath = []
    print(' ' * depth * 3, "   arrDown", arrDown, 'current dotori', dotori)
    for i in arrDown:
        subDotori, subPath = solve(list(arr), i, y+1, n, depth+1)
        # print(' ' * depth * 3, '      subDotori', subDotori, end="")
        # print(' subPath', subPath)
        subPath.insert(0, "D")
        move = abs(i-x)
        direction = "R" if i > x else "L"
        for j in range(move):
            subPath.insert(0, direction)

        if subMaxDotori <= subDotori:
            subMaxDotori = subDotori
            subMaxPath = subPath

    path.extend(subMaxPath)
    dotori += subMaxDotori
    print(' ' * depth * 3, '   dotori', dotori, end="")
    print(' path', path)
    return dotori, path


files = ['./input_8.txt']
for file in files:
    f = open(file)
    n = int(f.readline())
    arr = []
    for i in range(n):
        s = f.readline()
        arr.append(list(s))
    dotori, path = solve(arr, 0, 0, n, 0)
    print('dotori', dotori)
    print(''.join(path))
    f.close()
