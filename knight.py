input_data =input()             # 스트링 형식으로 받는다. 배열처럼 문자선택가능

cnt = 0 
row = int(input_data[1])
col = int(ord(input_data[0]) - (ord('a')-1))

col1 = int(col)
row1 = int(row)

action = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

for i in range(8):
    col += action[i][0]
    row += action[i][1]
    if col > 0 and col < 9 and row > 0 and row < 9:
        cnt += 1
        col = col1
        row = row1
    col = col1
    row = row1
        
    

print(cnt)