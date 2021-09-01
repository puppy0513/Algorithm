n, m ,k = map(int, input().split())         # n = number of input value m = total iteration , k = iteration of big number
data = list(map(int,input().split()))       # input array

data.sort()          # sort array as ascending

count = int (m/(k+1))*k 
count += int (m % (k+1))

result = data[n-1]*count + data[n-2]*(m-count)

print(result)