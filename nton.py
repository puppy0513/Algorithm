def change(n, q):
    rev_base = ''
    arr = []
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    rev_base = rev_base[::-1]

    arr = rev_base.split('0')
    return arr

def solution(n,k):
    print(answer)
    return answer

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True     

n,k = map(int, input().split())
a = change(n,k)
print(a)
val = len(a) - 1
i = 0

while True:  
    if a[i] == '1':
        del a[i]
        i = 0
    i += 1

    if i == val-1:
        break
a = list(filter(None, a))

answer =0

for i in range(len(a)):
    if is_prime_number(int(a[i])) == True:
        answer += 1
    else :
        continue

solution(n,k)