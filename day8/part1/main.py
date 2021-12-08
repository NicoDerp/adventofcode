with open('input','r') as f:
	#nums=list(map(lambda i:i.split('|'),f.read().split('\n')))
	nums=[]
	for s in f.read().split('\n'):
		if s=='':break
		a,b=s.split('|')
		if b[0]==' ':b=b[1:]
		if a[-1]==' ':a=a[:-1]
		nums.append([a.split(' '),b.split(' ')])

c=0
for i in nums:
	for n in i[1]:
		l=len(n)
		if l==2 or l==4 or l==3 or l==7:c+=1

print(c)
