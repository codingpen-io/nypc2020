'''

* 입력 : SSTT
* 출력 : 8

'''
s = input()

position = 0
for c in s:
    if c == 'S':
        position += 1
    elif c == 'T':
        position = (position//4 + 1) * 4

print(position)
