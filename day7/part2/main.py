def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

with open('input','r') as f:
	crabs=list(map(lambda i:int(i),f.read().split(',')))

#crabs=[16,1,2,0,4,2,7,1,2,14]
#print(crabs)
m=round(sum(crabs)/len(crabs))
#print(m)

def fuel(n):
	f=0
	for c in crabs:
		a=abs(n-c)+1
		b=a*(a-1)/2
		#print(c, m, b)
		f+=b
	return f

small,u=fuel(100),1000
for i in range(min(crabs),max(crabs)):
	small=min(small,a:=fuel(i))
	u=i if small==a else u

print(small)
print(u)
