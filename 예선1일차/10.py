n = int(input())


def solve(arr):
    op = ['+', '-', '*', '/', '.']
    for i in op:
        for j in op:
            if i == '.' and j == '.':
                continue
            if i == '/' and int(arr[1]) == 0:
                continue
            if j == '/' and int(arr[2]) == 0:
                continue
            s = arr[0] + i + arr[1] + j + arr[2]
            e = eval(s)
            print(s, e, abs(e - float(arr[3])))
            if abs(e - float(arr[3])) < 0.1:
                print(s + '=' + arr[3])
                return


for i in range(n):
    arr = input().split()
    solve(arr)
