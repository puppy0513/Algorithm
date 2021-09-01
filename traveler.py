n = int(input())

arr = [[0 for j in range(n)] for i in range(n)]         # N x N 2차원 배열 생성

m = input().split()
x = 1
y = 1

for i in range(len(m)):
    if m[i] == "R" and y < n:
        y +=1
    elif m[i] == "L" and y > 1:
        y -= 1
    elif m[i] == "U" and x > 1:
        x -= 1
    elif m[i] == "D" and x < n:
        x += 1

print (x, y)   