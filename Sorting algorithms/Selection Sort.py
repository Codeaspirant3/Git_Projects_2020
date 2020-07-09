
#Method 1 using third variable for swapping
array1=[1,7,2,9,0,3]

for i in range(len(array1)-1):
    min_index = i
    for j in range(i+1, len(array1)):
        if array1[j]<array1[min_index]:
            min_index = j
    temp = array1[i]
    array1[i]=array1[min_index]
    array1[min_index]= temp

print (array1)

#Method 2 using a,b = b,a (swapping)
array1=[1,7,2,9,0,3,25,-1]

for i in range(len(array1)-1):
    min_val = min(array1[i:])
    min_idx = array1.index(min_val)
    array1[i],array1[min_idx] = min_val,array1[i]

print(array1)

