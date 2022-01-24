import itertools

stuff = [1,4,2,5,3]
new = []
total_sum = 0

for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):

        if len(subset)%2 != 0:
            new.append(sum(list(subset)))

for i in new:
    total_sum += i

print(total_sum)