import sys
import re

a = sys.stdin.readline().rstrip().split('-')
sum =[]
b=[]

for i in a:
    cnt = 0
    b = i.split('+')
    for j in b:
        cnt += int(j)
    sum.append(cnt)

result = sum[0]

for i in range(1,len(sum)):
    result -= sum[i]

print(result)

#b = re.findall('\d+',a)
#c = re.findall('\W+', a)