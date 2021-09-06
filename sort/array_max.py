n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum = 0 
a = sorted(a)
b = sorted(b)

for i in range(k):
    if a[i] < b[k-1-i]:
        a[i] = b[n-1-i]
    else:
        break


for i in range(n):
    sum += a[i]

print(a)
print(sum)