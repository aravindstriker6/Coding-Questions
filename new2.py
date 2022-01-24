def new2(n,operations):
 a=[0 for i in range(n)]
 for i in operations:
     if "L" in i:
         for i in range(len(a)):
             if a[i]==0:
                 a[i]=1
                 break
             else:
                 continue

     elif "C" in i:
         a[int(i[1])]=0
 return a
print(new2(2,["L","L","L","C1"]))

