def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-1-i):

             if arr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
                 swap=True

        if swap==False:
            break
    return arr
array=[8,5,2,4,3,2]
print(bubble_sort(array))