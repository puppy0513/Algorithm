n,k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(int(input()))

result = 0 
i = 1
while True: 
    #for i in range(n):

    if k >= arr[n-i]:      # 끝에서부터 
        k -= arr[n-i]
        result += 1
    else: 
        i += 1

    if k ==0:
        print(result)
        break
