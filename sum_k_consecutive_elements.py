def consecutive_elements(arr,k):
    new=[]
    for i in range(len(arr)-k+1):
        sum=0
        for j in range(k):
            sum+=arr[j+i]
        new.append(sum)
    return max(new)
input=[10,6,9,8,6,2]
k=2
print(consecutive_elements(input,k))