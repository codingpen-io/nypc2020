
n = int(input())

score, count = map(int, input().split())

arrTemp = list(map(int, input().split()))

arr = []

for i in range(len(arrTemp)):
    arr.append({
        "no": i+1,
        "value": arrTemp[i],
        "diff": abs(arrTemp[i] - score)
    })

arr = sorted(arr, key=lambda x: (x['diff'], x['value']))

# import json
#print(json.dumps(arr, indent=2))

for i in range(count):
    x = arr[i]
    print(x['no'], end=' ')

print()
