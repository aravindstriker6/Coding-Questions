a=[1,2,3,4,5]
k=3
b=a[k-1::-1]
b.extend(a[-1:k-1:-1])
print(b)