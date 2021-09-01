n, m = map(int, input().split())

result = 0

while True:
    if n % m == 0 :
        n /= m
        result += 1
    else:
        n -= 1
        result += 1

    if n == 1: 
        break

print(result)