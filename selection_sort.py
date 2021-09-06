arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr,start,end):
    if start >= end: 
        return 

    pivot = start 
    left = start + 1
    right = end 

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start  and arr[right] >= arr[pivot]:
            right -= 1
        
        if right < left:
            arr[pivot], arr[right] = arr[right],arr[pivot]          # right , left가 서로 cross 하면 값을 바꿔준다.
        else:
            arr[left],arr[right] =arr[right],arr[left]              # 그렇지 않다면 서로의 값을 바꿔준다. 

    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)


quick_sort(arr,0,len(arr)-1)
print(arr)