def findMinDiff( A, N, M):
    A.sort()
    i=1
    for n in range(len(A)):
        if A[n]>=1:
          diff = A[n+M - 1] - A[n]
          maxi = diff
          break
        else:
            i=i+1


    for j in range(n+M, N):
        diff = A[j] - A[i]
        maxi = min(maxi, diff)
        i=i+1
    return maxi
print(findMinDiff([7,3,2,4,9,12,5,6],8,3))