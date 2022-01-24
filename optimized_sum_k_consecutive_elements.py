def consecutive_elements_opt(arr,k):
    window_sum=0

    for i in range(k):
        window_sum+=arr[i]
    max_sum=window_sum
    for j in range(k,len(arr)):
            window_sum=window_sum-arr[j-k]+arr[j]
            print(arr[j-k],arr[j])
            max_sum=max(max_sum,window_sum)
    return max_sum

input=[10,6,9,8,6,2]
k=2
print(consecutive_elements_opt(input,k))