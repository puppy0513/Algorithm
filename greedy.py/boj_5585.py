n = int(input())

a = 1000 - n
cnt = 0

while True:
    if a == 0:
        break
    elif a >= 500:
        cnt += 1
        a -= 500
        continue
    elif a >= 100:
        cnt += 1
        a -= 100
        continue
    elif a >= 50:
        cnt += 1
        a -= 50
        continue
    elif a >= 10:
        cnt += 1
        a -= 10
        continue
    elif a >= 5:
        cnt += 1
        a -= 5
        continue
    elif a >= 1:
        cnt += 1
        a -= 1
        continue
    
print(cnt)