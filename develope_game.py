import sys 
import numpy as np

n,m = map(int, input().split())         
x,y,di = map(int, input().split())

dx = [-1,0,1,0]             #북,동,남,서
dy = [0,1,0,-1]

arr = [list(map(int,input().split())) for _ in range(n)]     # 2차원 배열 입력받는법 꼭 외우고있기

arr[x][y] = 1               #방문했으니까 1로
dir_count = 0 
count = 1

while True:
    if di == 0:         # 방향 설정
        di = 3
    else:
        di -= 1

    nx = x + dx[di]     # 새 좌표 x,y값 설정
    ny = y + dy[di]

    # 새 좌표의 값 확인후 갱신
    if arr[nx][ny] == 0:        
        arr[nx][ny] = 1
        count += 1
        x,y = nx,ny
        dir_count = 0
        continue
    else:               # 바다일 경우
        dir_count += 1
        nx = x
        nx = y
    
    if dir_count == 4:      # 4면이 막혔을 경우에 이전 값으로 일단 돌아가
        nx = x - dx[di]
        ny = y - dy[di]

        if arr[nx][ny] == 0:
            x,y = nx ,ny
        else:
            break
        dir_count = 0

print(count, count)
    