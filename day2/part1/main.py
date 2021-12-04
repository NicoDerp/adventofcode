i=lambda a,b: a in b
with open('input','r') as f:
	p=0
	d=0
	for l in f:
		n=l.strip()[-1]
		if n=='':break
		n=int(n)
		if i('forward',l):p+=n
		if i('down',l):d+=n
		if i('up',l):d-=n
	print('a: {}, b: {}, ab: {}'.format(p,d,p*d))
