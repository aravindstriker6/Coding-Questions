def isAnagram( a, b):
    if len(a) != len(b):
        return "NO"
    else:
        c = {}
        d = {}
        for i in range(len(a)):
            if a[i] not in c:
                c[a[i]] = 1
            else:
                c[a[i]] += 1
            if b[i] not in d:
                d[b[i]] = 1
            else:
                d[b[i]] += 1
    for i in c:
        if i not in d:
            return "NO"
        else:
            if c[i] == d[i]:
                continue
            else:
                return "NO"
    return "YES"
print(isAnagram( "bood","doob"))
