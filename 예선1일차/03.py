'''
* 입력
3
10 5 3 9 18 3 2 2
11 3 1 1 8 7 8 7
5 3 2 4 6 8 9 4

* 출력
S
I
R

'''

n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    arr1 = arr[0:4]
    arr2 = arr[4:]
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    max1 = max(arr1)
    max2 = max(arr2)

    if sum1 > sum2 and max1 <= max2:
        print('S')
    elif max1 > max2 and sum1 <= sum2:
        print('I')
    else:
        print('R')
