arr = [2,3,6,8,9,1,0]

#Method1
for j in range(len(arr)-1):

    for i in range(len(arr)-j-1):
        try:
            if arr[i]>arr[i+1]:
                temp=arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=temp
        except:
            print("Exception occurred")

print(arr)

#method 2
arr = [2,3,6,8,9,1,0]
for j in range(len(arr)-1):
    flag =0  # to avoid redundant loops when the array is already sorted
    for i in range(len(arr)-j-1):
        try:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                flag =1
        except:
            print("Exception occurred")
    if flag==0:
        break

print(arr)