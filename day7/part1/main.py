def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

with open('input','r') as f:
	crabs=list(map(lambda i:int(i),f.read().split(',')))

#crabs=[16,1,2,0,4,2,7,1,2,14]

m=median(crabs)
f=0

for c in crabs:
	f+=abs(m-c)

print(f)
