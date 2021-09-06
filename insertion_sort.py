arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)):
    for j in range(i,0,-1):         # i 번째 숫자부터 0까지 숫자로 하나씩 줄어들면서 검사한다.
        if arr[j] < arr[j-1]:           
            arr[j],arr[j-1] =arr[j-1],arr[j]        # 뒤에서 부터 확인한기 시작한다.
        else: 
            break
print(arr)