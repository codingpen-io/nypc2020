import sys


def getHalf(begin, end):
    return int((begin+end)/2)


begin = 1
end = 1000
half = getHalf(1, 1000)

run = True
count = 1
while run:
    print(count, end=' : ')
    print(half)
    sys.stdout.flush()

    reply = input()

    if reply == 'CORRECT':
        run = False
    elif reply == 'UP':
        begin = half + 1
        half = getHalf(begin, end)
        if begin == half:
            print('bingo')
            half = end
    elif reply == 'DOWN':
        end = half - 1
        half = getHalf(begin, end)

    count += 1
    print("begin", begin, "half", half, "end", end)
