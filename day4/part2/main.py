with open('numbers','r') as f:
	nums=f.read().strip().split(',')

def solve(b,nums):
	l=[]
	r=b.copy()
	for n in nums:
		for i,_ in enumerate(b):
			#print('-{}-'.format(b[i]))
			for j,_ in enumerate(b[i]):
				for k,_ in enumerate(b[i][j]):
					#print('-{}-{}-{}-'.format(k,n,k==n))
					if b[i][j][k]==n:b[i][j][k]='x'+b[i][j][k]
				# Horizontals
				s=sum([1 for a in b[i][j] if 'x' in a])
				if b[i] in r and s==5:l=b[i];r.remove(b[i])
			# Verticals
			for x in range(5):
				s=sum([1 for y in b[i] if 'x' in y[x]])
				if b[i] in r and s==5:l=b[i];r.remove(b[i])
		if len(r)==0:return l,n

with open('boards','r') as f:
	boards=f.read().split('\n\n')
	boards=list(map(lambda i:[a.split(' ') for a in i.split('\n')],boards))
	for i,_ in enumerate(boards):
		for j,n in enumerate(boards[i]):
			boards[i][j] = [val for val in boards[i][j] if val!='']

	boards[-1].pop()

	board,num=solve(boards,nums)

	print(board)

	s=sum([sum([int(j) for j in i if 'x' not in j]) for i in board])
	print('sum: {}, num: {}, sum*num: {}'.format(s,num,s*int(num)))
