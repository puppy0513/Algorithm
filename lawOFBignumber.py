n, m ,k = map(int, input().split())         # n = number of input value m = total iteration , k = iteration of big number
data = list(map(int,input().split()))       # input array

data.sort()          # sort array as ascending
first = data[n-1]    # biggest number
second = data[n-2]   # second biggest number 
result = 0 

while True:
    for i in range(k):
        result += first
        m -= 1
    if first == second:
        for i in range(k):
            result += first
            m -= 1
    else:
        result += second
        m -= 1

    if m == 0:
        break

print(result)
