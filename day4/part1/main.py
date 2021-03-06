with open('numbers','r') as f:
	nums=f.read().strip().split(',')

def solve(b,nums):
	for n in nums:
		for i,_ in enumerate(b):
			#print('-{}-'.format(b[i]))
			for j,_ in enumerate(b[i]):
				for k,_ in enumerate(b[i][j]):
					#print('-{}-{}-{}-'.format(k,n,k==n))
					if b[i][j][k]==n:b[i][j][k]='x'+b[i][j][k]
				# Horizontals
				s=sum([1 for a in b[i][j] if 'x' in a])
				if s==5:return b[i],n
			# Verticals
			for x in range(5):
				s=sum([1 for y in b[i] if 'x' in y[x]])
				if s==5:return b[i],n

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
