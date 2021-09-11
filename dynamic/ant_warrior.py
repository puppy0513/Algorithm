import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

#최대값을 저장하는 배열
d =[0] * 100

d[0] =arr[0]
# arr의 1번,2번째 비교해서 업데이트
d[1] = max(arr[0],arr[1])

for i in range(2,n):
    d[i] =max(d[i-1],d[i-2]+arr[i])

print(d[n-1])


