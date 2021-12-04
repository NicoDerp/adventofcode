with open('numbers','r') as f:
	nums=f.read().strip().split(',')

with open('boards','r') as f:
	boards=f.read().split('\n\n')
	boards=list(map(lambda i:[a.split(' ') for a in i.split('\n')],boards))
	for i,_ in enumerate(boards):
		for j,n in enumerate(boards[i]):
			boards[i][j] = [val for val in boards[i][j] if val!='']
	#print(boards)
