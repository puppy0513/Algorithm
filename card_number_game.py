n, m = map(int, input().split())         # n = number of input value m = total iteration , k = iteration of big number
result =0

for i in range(n):
    data = list(map(int,input().split()))       # input array
    min_value = min(data)
    result = max(result, min_value)

print(result)