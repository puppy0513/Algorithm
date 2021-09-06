N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))

arr = sorted(arr,reverse= True)         # 역순으로 뽑는 거 OK?

print(arr)