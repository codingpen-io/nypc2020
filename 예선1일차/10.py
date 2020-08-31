n = int(input())


def solve(arr):
    op = ['+', '-', '*', '/', '.']
    for i in op:
        for j in op:
            if i == j:
                continue
            s = arr[0] + i + arr[1] + j + arr[2]
            if eval(s) == float(arr[3]):
                print(s + '=' + arr[3])
                return


for i in range(n):
    arr = input().split()
    solve(arr)
