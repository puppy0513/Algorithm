import sys

n = int(input())
arr =[]
d =[0]*11

d[0] =1
d[1] =2
d[2] =4

for i in range(n):
    val = int(input())
    arr.append(val)

for i in range(3,11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in range(n):
    print(d[arr[i]-1])
