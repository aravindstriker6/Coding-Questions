def minimumPlatform( n, arr, dep):
    arr.sort()
    dep.sort()
    maxi = 1
    pl = 1
    s = 1
    e = 0
    while s <n:

        if arr[s] <= dep[e]:
            pl += 1
            maxi = max(maxi, pl)
            s = s + 1
        else:
            pl -= 1
            e = e + 1
    return maxi
print(minimumPlatform( 6, [900,940,950,1100,1500,1800], [910 ,1200 ,1120 ,1130 ,1900 ,2000]))