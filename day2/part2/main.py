i=lambda a,b: a in b
with open('input','r') as f:
	a,p,d=0,0,0
	for l in f:
		n=l.strip()[-1]
		if n=='':break
		n=int(n)
		if i('forward',l):p+=n;d+=a*n
		if i('down',l):a+=n
		if i('up',l):a-=n
	print('a: {}, b: {}, ab: {}'.format(p,d,p*d))
