arr= [2,3,9,8,4]

for i in range(1,len(arr)):
    val =arr[i]
    for j in range(i-1,-1,-1):
        if arr[j] > arr[i]:
            arr[j],arr[j+1]=val,arr[j]
print(arr)


