with open('small','r') as f:
	riskmap=f.read().split('\n')

riskmap.pop()

def getNeighbours(x, y, size):
	if x!=0: yield (x-1, y)
	if x!=size-1: yield (x+1, y)
	if y!=0: yield (x, y-1)
	if y!=size-1: yield (x, y+1)

riskmapsize=len(riskmap)

x,y=0,0
while True:
	neighbours=getNeighbours(x,y,riskmapsize)
	minv=10
	mincoords=[0,0]
	for n in neighbours:
		val=int(riskmap[n[0]][n[1]])
		if val<minv:
			minv=val
			mincoords=n
	print(mincoords)

print(riskmap)
print(len(riskmap))
print(len(riskmap[0]))
