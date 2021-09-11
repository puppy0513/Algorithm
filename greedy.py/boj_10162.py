n = int(input())

a,b,c = 300,60,10

cnt =[0,0,0]

while True:
    if n >= 300:
        cnt[0] += 1
        n -= 300
        continue
    elif n >= 60:
        cnt[1] += 1
        n -= 60
        continue
    elif n >= 10:
        cnt[2] += 1
        n -= 10
        continue
    elif n < 10 and n!= 0:
        print(-1)
        break
    elif n == 0:
        for i in cnt:
            print(i ,end =' ')
        break



