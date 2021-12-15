def printPositions(positions):
	maxx=0
	maxy=0

	for pos in positions:
		maxx=max(pos[0],maxx)
		maxy=max(pos[1],maxy)

	map=[['.' for _ in range(maxy+1)] for _ in range(maxx+1)]
	for pos in positions:
		map[pos[0]][pos[1]]='#'

	for x in map:
		print(x)


with open('small','r') as f:
	positions,folds=f.read().split('\n\n')

positions=positions.split('\n')
folds=folds.split('\n')
folds.pop()

positions=list(map(lambda i:[int(j) for j in i.split(',')], positions))
folds=list(map(lambda i:[i[11],int(i[13:])], folds))


#print(positions)
print(folds)
printPositions(positions)

for fold in folds:
	if fold[0]=='y':
		new=[]
		for pos in positions:
			# Under line
			if pos[1]<fold[1]:
				x,y = pos[0], fold[1]-pos[1]
				if not [x,y] in new:
					new.append([x,y])
			else:
				new.append(pos)
		positions=new
	break

# Prints positions
print('a')
printPositions(positions)
