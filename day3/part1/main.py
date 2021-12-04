with open('input','r') as f:
	#   0 1
	a=[[0,0] for _ in range(12)]
	for l in f:
		s=l.strip()
		for i,n in enumerate(s):
			a[i][0 if n=='0' else 1]+=1
	#[print(n) for n in a]
	epsilon = int(''.join(['1' if n[0]>n[1] else '0' for n in a]),2)
	gamma = int(''.join(['0' if n[0]>n[1] else '1' for n in a]),2)
	print('epsilon: {}, gamma: {}, {}'.format(epsilon, gamma, epsilon*gamma))
