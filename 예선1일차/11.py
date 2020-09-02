'''
# 입력
5
00:30:00
00:31:00
00:32:00
00:33:00
00:50:00

#출력
2
'''


from sys import maxunicode


def time_to_sec(time):
    arr = list(map(int, time.split(":")))
    return arr[0] * 60 * 60 + arr[1] * 60 + arr[2]


n = int(input())

arrTime = []
for i in range(n):
    arrTime.append(time_to_sec(input()))

allPairs = []


def pick(arr, current):
    #print("arr", arr, "current", current)
    if len(arr) < 2:
        allPairs.append(current[:])
        return

    first = arr.pop(0)
    for i in range(len(arr)):
        arrTemp = arr[:]
        second = arrTemp.pop(i)
        current.append([first, second])
        pick(arrTemp, current)
        current.pop()


if len(arrTime) == 1:
    print('0')
else:
    pick(arrTime, [])
    sumResults = []
    for pairs in allPairs:
        arr = []
        sumResults.append(arr)
        for pair in pairs:
            #print('sum', sum(pair), 'pair', pair)
            arr.append(sum(pair))

    maxCount = 0
    for result in sumResults:
        myMin = min(result)
        # print('---', myMin, 'result', result)
        count = 0
        for x in result:
            if x - myMin <= 1000:
                count += 1
        if count > maxCount:
            maxCount = count

    print(maxCount)
