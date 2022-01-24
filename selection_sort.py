def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                arr[j],arr[min_index]=arr[min_index],arr[j]
            else:
                continue
    return arr

array=[8,5,2,4,3,2]
print(selection_sort(array))
