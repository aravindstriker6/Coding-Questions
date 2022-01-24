def subArraySum( arr, n, s):
    for i in range(n):
        sum = arr[i]
        for j in range(i+1, n):
            sum += arr[j]

            if sum == s:
                return [i + 1, j + 1]
    return [-1]
print(subArraySum( [1,2,3,7,5],5,12))