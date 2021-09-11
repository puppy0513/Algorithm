n = int(input())

a = []
result =[]
value = 0


for i in range(n):
    value = int(input())
    a.append(value)

a.sort(reverse=True)


for i in range(n):
    value = a[i] * (i+1)
    result.append(value)

print(max(result))
    