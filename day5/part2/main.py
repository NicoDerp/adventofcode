# Gets x,y values seperated by comma and converts to int
getvals=lambda a,b:list(map(lambda i:int(i),a[b].split(',')))

# Better Range can also automatically go backwards
brange=lambda a,b:range(a,b+1) if a<b else range(a,b-1,-1)

with open('input','r') as f:
	# Into format [[from,to],[from,to],...,[from,to]]
	v=list(map(lambda i:i.split(' -> '),f.read().split('\n')))
	# Remove empty list at end
	v.pop()

	w=0
	h=0
	# Set up map
	for xy in v:
		#print(xy)
		x1,y1=getvals(xy,0)
		x2,y2=getvals(xy,1)

		w=max(w,max(x1,x2))
		h=max(h,max(y1,y2))

	m = [[0 for _ in range(w+1)] for _ in range(h+1)]

	for xy in v:
		x1,y1=getvals(xy,0)
		x2,y2=getvals(xy,1)

		minx=min(x1,x2)
		maxx=max(x1,x2)

		miny=min(y1,y2)
		maxy=max(y1,y2)


		# Horizontal
		if y1==y2:
			#print('x',minx,maxx)
			for x in range(minx,maxx+1):
				m[x][y1]+=1
		# Vertical
		elif x1==x2:
			#print('y',miny,maxy)
			for y in range(miny,maxy+1):
				m[x1][y]+=1
		# Diagonal, 45 degrees
		elif abs(x1-x2)==abs(y1-y2):
			for x,y in zip(brange(x1,x2),brange(y1,y2)):
				#print(x,y)
				m[x][y]+=1
		else:print('not straight lines', x1, y1, ',', x2, y2)

	c=0
	for i in reversed(m):
		for j in i:
			print(j if j!=0 else '.',' ',end='')
			if j>1:c+=1
		print()
	print('Count: ',c)
