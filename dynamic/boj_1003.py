import sys 

# 방문 횟수
d =[0]* 41

def fibo(n):
    
    if d[n] != 0:
        return d[n]

    if n < 2:
        return n
    else:
        d[n] = fibo(n-1)+fibo(n-2) 
        return d[n]


T = int(sys.stdin.readline().rstrip())

for i in range(T):
    case = int(sys.stdin.readline().rstrip())
    #예외 두개 (0,1)처리
    if case == 0:
        print(1,0)
    elif case == 1:
        print(0,1)
    else:           
        print(fibo(case-1),fibo(case))