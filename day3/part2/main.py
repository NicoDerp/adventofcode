with open('input','r') as f:
	ox=f.read().split('\n')[:-1]
	co=ox.copy()
	for i in range(0,12):
		c=[0,0]
		for l in ox:
			c[int(l[i])]+=1

		hox='0' if c[0]>c[1] else '1'
		ox=list(filter(lambda l: l[i]==hox,ox))

		if len(co)==1:continue
		c=[0,0]
		for l in co:
			c[int(l[i])]+=1

		lco=str(1-(0 if c[0]>c[1] else 1))
		co=list(filter(lambda l: l[i]==lco,co))
		print('{}, {}'.format(c,lco))

		if len(ox)==1 and len(co)==1:break

	ox = int(ox[0],2)
	co = int(co[0],2)
	print('ox: {}, co: {}, life: {}'.format(ox,co,ox*co))

