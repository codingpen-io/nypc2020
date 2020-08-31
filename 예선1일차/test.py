import json
arr = []

arr.append({
    'name': 'jin',
    'score': 10,
    'age': 10
})

arr.append({
    'name': 'cho',
    'score': 10,
    'age': 9
})

arr.append({
    'name': 'joa',
    'score': 8,
    'age': 8
})

#print(json.dumps(arr, indent=2))

# 점수만 높은 사람이 뒤에 오게
# arr1 = sorted(arr, key=lambda x: x['score'])
# print(json.dumps(arr1, indent=2))

# # 점수가 높은 사람이 뒤에 오고 같은 점수이면 나이가 높은 사람이 뒤에 오게
# arr2 = sorted(arr, key=lambda x: (x['score'], x['age']))
# print(json.dumps(arr2, indent=2))

# # 점수가 높은 사람이 뒤에 오고 같은 점수이면 나이가 낮은 사람이 뒤에 오게
# arr2 = sorted(arr, key=lambda x: (x['score'], -x['age']))
# print(json.dumps(arr2, indent=2))


# def test(arr):
#     arr.append(1)
#     arr.append(2)


# myarr = []

# test(myarr)

# print(myarr)

arr = ['1', '2', '3']

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
        print(s, eval(s))
