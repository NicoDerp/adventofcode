from itertools import product

with open('input','r') as f:
	lines=f.read().split('\n')
	lines.pop()

def _neighbours(cell,size):
	for c in product(*(range(n-1, n+2) for n in cell)):
		if c != cell and all(0 <= n < size for n in c):
			yield c

def neighbours(x,y,s):
	return [(x+a[0], y+a[1]) for a in
		[(-1,0), (1,0), (0,-1), (0,1)]
		if ((0 <= x+a[0] < s) and (0 <= y+a[1] < s))]

basins={}
for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j]=='9':continue
		low_coords=[10,10]
		lowest=10
		for n in neighbours(i,j,len(lines)):
			v=int(lines[n[0]][n[1]])
			if v<lowest:
				lowest=v
				low_coords[0]=i
				low_coords[1]=j
		print(low_coords)
