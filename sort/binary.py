def binary_sort(arr, tar, start, end):
    if start >= end:
        return None
    mid = (start + end) // 2

    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return binary_sort(arr,tar,start,mid-1)
    else:
        return binary_sort(arr,tar, mid+1, end)

n,target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_sort(array,target,0,n-1)

if result == None: 
    print("원소가 존재하지 않는다.")
else: 
    print(result+1)


