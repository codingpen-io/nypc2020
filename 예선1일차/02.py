'''
* 입력
01:00:00
00:50:00
00:40:00
6
01:00:00
00:49:99
00:30:00
00:45:00
00:55:00
01:00:01

* 출력
*
**
***
**
*
:(

'''


def time_to_seconds(t):
    arr = list(map(int, t.split(":")))
    s = arr[0] * 60 * 100 + arr[1] * 100 + arr[2]
    return s


t1 = time_to_seconds(input())
t2 = time_to_seconds(input())
t3 = time_to_seconds(input())


def get_star(s):
    if s <= t3:
        return 3
    elif s <= t2:
        return 2
    elif s <= t1:
        return 1
    else:
        return 0


n = int(input())

for i in range(n):
    s = time_to_seconds(input())
    star = get_star(s)
    if star > 0:
        print('*' * star)
    else:
        print(':(')
