'''
N개의 정수로 이루어진 배열이 주어진다. 이 배열의 최대구간합을 구하는 프로그램을 작성하시오.

예를 들어, 배열이 [2, 5, -9, 7, 3, -2, 5] 인 경우, 
네 번째 값부터 일곱 번째 값까지 해당하는 구간의 합은 1313이며 구간합 중 가장 큰 값이 되므로 
최대구간합은 1313이 된다.

입력 형식
입력의 첫 줄에 배열의 크기 NN이 주어진다. (1 <= N <= 1 000 000)

둘째 줄에 배열의 내용을 나타내는 NN개의 정수가 공백으로 구분되어 주어진다. 주어지는 정수의 절대값은 10^9보다 크지 않다.

출력 형식
첫 줄에 최대구간합을 출력한다.

입력 예제
```
7
2 5 -9 7 3 -2 5
```

출력예제
```
13
```
'''

# # 방법 1 브루트 포스
# n = int(input())
# arr = list(map(int, input().split()))

# max_sum = 0
# for i in range(n):
#     s = 0
#     for j in range(i, n):
#         s += arr[j]

#     if s > max_sum:
#         max_sum = s

# print(max_sum)

# 방법2 dynamic programming
# 30점 짜리
# n = int(input())
# arr = list(map(int, input().split()))

# memo = [None] * n
# memo[0] = arr[0]

# for i in range(1, n):
#     memo[i] = max(0, memo[i-1]+arr[i])

# print(max(memo))

# 방법3
# n = int(input())
# arr = list(map(int, input().split()))

# memo = [None] * n
# memo[0] = arr[0]

# myMax = memo[0]
# for i in range(1, n):
#     memo[i] = max(0, memo[i-1]+arr[i])
#     if memo[i] > myMax:
#         myMax = memo[i]


# print(myMax)

'''
n = int(input())
arr = list(map(int, input().split()))

memo = [None] * n
memo[0] = arr[0]

myMax = memo[0]
for i in range(1, n):
    memo[i] = max(arr[i], memo[i-1]+arr[i])
    # if memo[i] > myMax:
    #     myMax = memo[i]
    myMax = max(memo[i], myMax)


print(myMax)

'''

# 위 풀이를 보면 메모한 값을 바로 이전 값 만 사용하는 것을 알 수 있다
# 이 경우 굳이 어레이로 저장하지 않고, 단일 변수만으로
# 이전 최대 구간합을 myLastMax로 저장해서 사용하는 식으로 더 메모리 사용량을
# 줄일 수 있다.
n = int(input())
arr = list(map(int, input().split()))

myLastMax = myMax = arr[0]

for a in arr[1:]:
    myLastMax = max(a, myLastMax + a)
    myMax = max(myLastMax, myMax)

print(myMax)
