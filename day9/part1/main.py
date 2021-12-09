with open('input','r') as f:
	lines=f.read().split('\n')
	lines.pop()

s=0
for i,l in enumerate(lines):
	for j,n in enumerate(l):
		top=-1 if i==0 else lines[i-1][j]
		bottom=-1 if i==len(lines)-1 else lines[i+1][j]
		left=-1 if j==0 else l[j-1]
		right=-1 if j==len(l)-1 else l[j+1]

		adj=[]
		if top!=-1:adj.append(top)
		if bottom!=-1:adj.append(bottom)
		if left!=-1:adj.append(left)
		if right!=-1:adj.append(right)

		print(adj)
		a=0
		for k in adj:
			if int(n)<int(k):a+=1

		if a==len(adj):
			print(n)
			s+=int(n)+1
print(s)
