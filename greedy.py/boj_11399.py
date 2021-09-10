import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().strip().split()))
arr.sort()
result = 0
result1 = 0

for i in range(n):
    result = result +arr[i]
    result1 += result

print(result1)