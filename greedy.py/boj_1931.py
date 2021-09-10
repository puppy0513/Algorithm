import sys 
input = sys.stdin.readline

cnt = 0 
last = 0
N = int(input())
meeting = []

for i in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting = sorted(meeting, key = lambda item:item[0])
meeting = sorted(meeting, key = lambda item:item[1])


cnt = 1 
end_time = meeting[0][1]
for i in range(1, N): 
    if meeting[i][0] >= end_time: 
        cnt += 1 
        end_time = meeting[i][1] 
        

print(cnt)

