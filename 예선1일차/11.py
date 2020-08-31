'''
5
00:30:00
00:31:00
00:32:00
00:33:00
00:50:00
'''


def time_to_sec(time):
    arr = list(map(int, time.split(":")))
    return arr[0] * 60 * 60 + arr[1] * 60 + arr[2]


n = int(input())

arrTime = []
for i in range(n):
    arrTime.append(time_to_sec(input()))

arrT
for t1 in arrTime:
    for t2 in arrTime:
        if t1
