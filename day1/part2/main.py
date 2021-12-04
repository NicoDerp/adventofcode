r = lambda file: file.readline().strip()
with open('input','r') as f:
	A=[int(r(f)) for _ in [0,0,0]]
	B=[]
	c=0
	while 1:
		l=r(f)
		if l=='':break
		B=[A[1], A[2], int(l)]
		if sum(A)<sum(B):c+=1
		A=B
	print(c)
