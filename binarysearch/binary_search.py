import sys 

def binary_search(arr, tar, start, end):
    while start <= end:
        mid = int((start + end) /2)
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            end = mid-1
        else:
            start = mid+1
    return None


a = int(input())

array = list(map(int,sys.stdin.readline().rstrip().split()))
array.sort()

m = int(input())
target = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(m):
    result = binary_search(array,target[i],0,a-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')